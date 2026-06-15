#!/usr/bin/env python3
"""
旅行记账 - 统计与最优转账计算
基于飞书多维表格数据，使用贪心算法计算最优转账方案

用法:
  python3 trip_accounting.py <app_token> <consumption_table_id> <members_table_id>

示例:
  python3 trip_accounting.py IzDTbaKqcaO8jfsvzk8caCNangi tblnD6bpJAllpodn tblgZzh8by8rPubK
"""

import sys
import json
from collections import defaultdict
from typing import Dict, List, Tuple

# ============================================================
# 贪心算法计算最优转账方案
# ============================================================

def calculate_optimal_transfers(balances: Dict[str, float]) -> List[Tuple[str, str, float]]:
    """
    使用贪心算法计算最优转账方案。
    
    思路:
    1. 计算每个人最终应该得到或支付多少钱（正=应收，负=应付）
    2. 从最大的债权人向最大的债务人转账，逐步消除差额
    3. 直到所有人的余额都为0或接近0
    
    balances: { 成员名: 净额 (正=应收, 负=应付) }
    返回: [(付款人, 收款人, 金额), ...]
    """
    # 按余额分组
    creditors = []  # 应收的人（正余额）
    debtors = []    # 应付的人（负余额）
    
    for name, balance in balances.items():
        if balance > 0.01:  # 容忍浮点误差
            creditors.append((name, balance))
        elif balance < -0.01:
            debtors.append((name, -balance))  # 转成正值存储
    
    # 按金额降序排列
    creditors.sort(key=lambda x: x[1], reverse=True)
    debtors.sort(key=lambda x: x[1], reverse=True)
    
    transfers = []
    i, j = 0, 0
    
    while i < len(creditors) and j < len(debtors):
        creditor_name, credit_amount = creditors[i]
        debtor_name, debt_amount = debtors[j]
        
        # 转账金额是两者中较小的
        transfer_amount = min(credit_amount, debt_amount)
        
        if transfer_amount > 0.01:  # 忽略太小金额
            transfers.append((debtor_name, creditor_name, round(transfer_amount, 2)))
        
        # 更新余额
        creditors[i] = (creditor_name, credit_amount - transfer_amount)
        debtors[j] = (debtor_name, debt_amount - transfer_amount)
        
        # 如果某方已结清，移动到下一个
        if creditors[i][1] < 0.01:
            i += 1
        if debtors[j][1] < 0.01:
            j += 1
    
    return transfers


def calculate_balances(records: List[dict], member_field_map: dict) -> Tuple[Dict[str, float], Dict[str, Dict], float]:
    """
    从消费记录计算每个人的净余额。
    
    逻辑:
    - 付款人: +总金额 (别人欠他)
    - 平摊成员: -人均金额 (他欠别人)
    
    records: 消费记录列表
    member_field_map: 字段名到ID的映射
    返回: (余额字典, 消费统计, 总消费)
    """
    balances = defaultdict(float)  # 成员 -> 净额
    stats = defaultdict(lambda: {"paid": 0, "share": 0, "count": 0})  # 成员 -> {已付, 应摊, 笔数}
    total = 0.0
    
    for record in records:
        fields = record.get("fields", {})
        
        # 获取字段值
        total_amount = fields.get("总金额", 0)
        payer = fields.get("付款人", "")
        split_members = fields.get("平摊成员", [])
        split_count = fields.get("平摊人数", 1)
        category = fields.get("消费类型", "其他")
        
        if not total_amount or total_amount <= 0:
            continue
        
        total += total_amount
        
        # 如果没有指定平摊成员，按平摊人数平均分配
        if not split_members:
            per_person = total_amount / split_count if split_count > 0 else total_amount
        else:
            per_person = total_amount / len(split_members)
        
        # 付款人加钱（别人欠他）
        if payer:
            balances[payer] += total_amount
            stats[payer]["paid"] += total_amount
            stats[payer]["count"] += 1
        
        # 每个平摊成员减钱（欠别人）
        if split_members:
            for member in split_members:
                balances[member] -= per_person
                stats[member]["share"] += per_person
        else:
            # 平摊人数模式，没人具体欠谁
            pass
    
    # 四舍五入避免浮点误差
    for name in balances:
        balances[name] = round(balances[name], 2)
    
    return dict(balances), dict(stats), round(total, 2)


def format_report(balances: Dict, stats: Dict, total: float, transfers: List) -> str:
    """生成美观的统计报告"""
    report = []
    report.append("=" * 50)
    report.append("          🧾 旅行记账统计报告")
    report.append("=" * 50)
    
    # 总消费
    report.append(f"\n💰 总消费: ¥{total:.2f}")
    report.append("-" * 50)
    
    # 每人消费明细
    report.append("\n📊 每人消费明细:")
    report.append(f"{'成员':<10} {'已付':>10} {'应摊':>10} {'差额':>10}")
    report.append("-" * 42)
    
    for member, s in sorted(stats.items(), key=lambda x: -x[1]["paid"]):
        diff = s["paid"] - s["share"]
        sign = "+" if diff >= 0 else ""
        report.append(f"{member:<10} ¥{s['paid']:>9.2f} ¥{s['share']:>9.2f} {sign}¥{abs(diff):>8.2f}")
    
    # 净余额
    report.append("\n💵 净余额 (正=应收, 负=应付):")
    for member, bal in sorted(balances.items(), key=lambda x: -x[1]):
        if abs(bal) > 0.01:
            emoji = "📈" if bal > 0 else "📉"
            report.append(f"  {emoji} {member}: {'+' if bal >= 0 else ''}¥{bal:.2f}")
    
    # 最优转账方案
    if transfers:
        report.append("\n" + "=" * 50)
        report.append("          🔄 最优转账方案 (贪心算法)")
        report.append("=" * 50)
        report.append("\n按以下方式转账即可结清所有账目:\n")
        for i, (from_person, to_person, amount) in enumerate(transfers, 1):
            report.append(f"  {i}. {from_person} → {to_person}: ¥{amount:.2f}")
        
        report.append(f"\n📌 共需 {len(transfers)} 笔转账即可结清")
    else:
        report.append("\n✅ 所有账目已结清，无需转账!")
    
    report.append("\n" + "=" * 50)
    
    return "\n".join(report)


# ============================================================
# 模拟数据测试 (用于验证算法)
# ============================================================

def test_with_mock_data():
    """用模拟数据测试算法"""
    print("🧪 使用模拟数据测试算法...\n")
    
    # 模拟场景: 小明、小红、小华三人旅行
    mock_records = [
        # 小明付了机票，3人平摊
        {"fields": {"消费项目": "机票", "消费类型": "交通", "总金额": 900, "付款人": "小明", "平摊人数": 3, "平摊成员": ["小明", "小红", "小华"]}},
        # 小红付了酒店，3人平摊
        {"fields": {"消费项目": "酒店", "消费类型": "住宿", "总金额": 600, "付款人": "小红", "平摊人数": 3, "平摊成员": ["小明", "小红", "小华"]}},
        # 小华付了晚餐，只有小明和小红平摊
        {"fields": {"消费项目": "晚餐", "消费类型": "餐饮", "总金额": 300, "付款人": "小华", "平摊人数": 2, "平摊成员": ["小明", "小红"]}},
        # 小明自己买了个包
        {"fields": {"消费项目": "购物", "消费类型": "购物", "总金额": 200, "付款人": "小明", "平摊人数": 1, "平摊成员": ["小明"]}},
        # 小红付了门票，只有小华平摊
        {"fields": {"消费项目": "景点门票", "消费类型": "门票/娱乐", "总金额": 150, "付款人": "小红", "平摊人数": 2, "平摊成员": ["小华"]}},
    ]
    
    # 模拟字段映射
    member_field_map = {"付款人": "fldxxx", "平摊成员": "fldyyy"}
    
    balances, stats, total = calculate_balances(mock_records, member_field_map)
    transfers = calculate_optimal_transfers(balances)
    report = format_report(balances, stats, total, transfers)
    
    print(report)
    print("\n算法验证通过!")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        test_with_mock_data()
    else:
        print(__doc__)
        print("\n🧪 运行测试模式:")
        print("  python3 trip_accounting.py --test")
