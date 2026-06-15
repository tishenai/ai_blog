#!/usr/bin/env python3
"""
旅行记账 - 命令解析与交互
处理用户的记账命令，增删改查消费记录
"""

import sys
import json
import os
from typing import Optional, Dict, List, Any
from datetime import datetime

# 添加父目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from trip_accounting import calculate_balances, calculate_optimal_transfers, format_report

# 消费类型选项
CONSUMPTION_TYPES = ["餐饮", "交通", "住宿", "门票/娱乐", "购物", "其他"]

# 飞书多维表格配置
BITABLE_APP_TOKEN = "IzDTbaKqcaO8jfsvzk8caCNangi"
MEMBERS_TABLE_ID = "tblgZzh8by8rPubK"
CONSUMPTION_TABLE_ID = "tblnD6bpJAllpodn"

# 字段ID映射（需要从API获取）
FIELD_MAP = {
    "消费项目": "fldLICQmHg",
    "消费类型": "fld0naa9UY", 
    "总金额": "fldJ4iu3EJ",
    "付款人": "fld1Ieeihj",
    "平摊人数": "fldOkHqUKm",
    "平摊成员": "fldYx4qJyR",
    "人均金额": "fldskxOZ7E",
    "付款日期": "fldFcwEgh3",
    "备注": "fldy6AHPiu",
    "结算状态": "fldbT5FUuv",
}


def parse_add_command(args: List[str]) -> Dict[str, Any]:
    """
    解析 /add 命令
    格式: /add 消费项目 消费类型 金额 付款人 平摊人数 [平摊成员...]
    
    示例: /add 晚餐 餐饮 300 小明 3 小明,小红,小华
    """
    if len(args) < 5:
        return {"error": "参数不足！格式：/add 消费项目 消费类型 金额 付款人 平摊人数 [平摊成员]"}
    
    project = args[0]
    category = args[1]
    try:
        amount = float(args[2])
    except ValueError:
        return {"error": f"金额必须是数字，当前值：{args[2]}"}
    
    payer = args[3]
    try:
        split_count = int(args[4])
    except ValueError:
        return {"error": f"平摊人数必须是数字，当前值：{args[4]}"}
    
    # 平摊成员（可选，逗号分隔）
    split_members = []
    if len(args) > 5:
        split_str = args[5]
        split_members = [m.strip() for m in split_str.split(",") if m.strip()]
    
    # 验证消费类型
    if category not in CONSUMPTION_TYPES:
        return {"error": f"消费类型必须是以下之一：{', '.join(CONSUMPTION_TYPES)}"}
    
    # 计算人均金额
    if split_members:
        per_person = round(amount / len(split_members), 2)
    elif split_count > 0:
        per_person = round(amount / split_count, 2)
    else:
        per_person = amount
    
    return {
        "success": True,
        "record": {
            "消费项目": project,
            "消费类型": category,
            "总金额": amount,
            "付款人": payer,
            "平摊人数": split_count,
            "平摊成员": split_members,
            "人均金额": per_person,
            "付款日期": int(datetime.now().timestamp() * 1000),
            "结算状态": "待结算"
        }
    }


def format_add_confirmation(result: Dict) -> str:
    """格式化添加确认信息"""
    if "error" in result:
        return f"❌ {result['error']}"
    
    r = result["record"]
    msg = []
    msg.append("✅ 消费记录已添加！")
    msg.append("")
    msg.append(f"📝 项目：{r['消费项目']}")
    msg.append(f"🏷️ 类型：{r['消费类型']}")
    msg.append(f"💰 金额：¥{r['总金额']:.2f}")
    msg.append(f"👤 付款人：{r['付款人']}")
    
    if r['平摊成员']:
        msg.append(f"👥 平摊成员：{', '.join(r['平摊成员'])} ({len(r['平摊成员'])}人)")
    else:
        msg.append(f"👥 平摊人数：{r['平摊人数']}人")
    
    msg.append(f"💵 人均：¥{r['人均金额']:.2f}")
    
    return "\n".join(msg)


def build_stats_message(records: List[Dict]) -> str:
    """构建统计消息"""
    if not records:
        return "📭 暂无消费记录，快来添加第一笔吧！"
    
    balances, stats, total = calculate_balances(records, {})
    transfers = calculate_optimal_transfers(balances)
    
    return format_report(balances, stats, total, transfers)


def build_help_message() -> str:
    """构建帮助信息"""
    help_text = """
📖 **旅行记账命令帮助**

**添加消费记录**
```
/add 项目 类型 金额 付款人 平摊人数 [平摊成员...]
```
示例：
• `/add 晚餐 餐饮 300 小明 3 小明,小红,小华` - 3人平摊晚餐
• `/add 机票 交通 900 小明 3 小明,小红,小华` - 3人平摊机票
• `/add 门票 门票 150 小红 2 小明,小华` - 小明小华平摊门票
• `/add 购物 购物 200 小明 1 小明` - 小明个人消费

**查看统计**
```
/stats
```
显示总消费、每人消费明细、净余额、最优转账方案。

**一键平账**
```
/settle
```
查看最优转账方案，谁该给谁多少钱。

**添加成员**
```
/addmember 张三
```

**删除成员**
```
/delmember 张三
```

**查看帮助**
```
/help
```

---
💡 消费类型：餐饮、交通、住宿、门票/娱乐、购物、其他
"""
    return help_text.strip()


if __name__ == "__main__":
    # 测试命令解析
    test_args = ["晚餐", "餐饮", "300", "小明", "3", "小明,小红,小华"]
    result = parse_add_command(test_args)
    print(format_add_confirmation(result))
    print()
    print(build_help_message())
