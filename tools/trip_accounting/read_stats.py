#!/usr/bin/env python3
"""
旅行记账 - 读取飞书表格并生成统计报告
直接从飞书多维表格读取数据，生成统计和转账方案
"""

import sys
import os
import json
import argparse

# 添加父目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from trip_accounting import calculate_balances, calculate_optimal_transfers, format_report

# 飞书配置
DEFAULT_APP_TOKEN = "IzDTbaKqcaO8jfsvzk8caCNangi"
DEFAULT_MEMBERS_TABLE = "tblgZzh8by8rPubK"
DEFAULT_CONSUMPTION_TABLE = "tblnD6bpJAllpodn"


def read_feishu_table(app_token: str, table_id: str, page_size: int = 100) -> list:
    """
    通过飞书 API 读取多维表格数据
    使用 subprocess 调用 curl 命令
    """
    import subprocess
    
    # 读取所有记录
    cmd = [
        "curl", "-s", "-X", "GET",
        f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records",
        "-H", f"Authorization: Bearer {os.environ.get('FEISHU_ACCESS_TOKEN', '')}",
        "-H", "Content-Type: application/json"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        data = json.loads(result.stdout)
        
        if data.get("code") != 0:
            print(f"读取失败: {data.get('msg')}")
            return []
        
        records = data.get("data", {}).get("items", [])
        
        # 检查是否还有更多数据
        while data.get("data", {}).get("has_more"):
            page_token = data.get("data", {}).get("page_token", "")
            cmd[-1] = f"{cmd[-1]}?page_token={page_token}"
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            data = json.loads(result.stdout)
            records.extend(data.get("data", {}).get("items", []))
        
        return records
    except Exception as e:
        print(f"API 调用失败: {e}")
        return []


def main():
    parser = argparse.ArgumentParser(description="旅行记账统计")
    parser.add_argument("--app-token", default=DEFAULT_APP_TOKEN, help="飞书 App Token")
    parser.add_argument("--table", default=DEFAULT_CONSUMPTION_TABLE, help="消费记录表 ID")
    parser.add_argument("--members-table", default=DEFAULT_MEMBERS_TABLE, help="成员表 ID")
    parser.add_argument("--test", action="store_true", help="使用模拟数据测试")
    
    args = parser.parse_args()
    
    if args.test:
        # 使用模拟数据测试
        mock_records = [
            {"fields": {"消费项目": "机票", "消费类型": "交通", "总金额": 900, "付款人": "小明", "平摊人数": 3, "平摊成员": ["小明", "小红", "小华"]}},
            {"fields": {"消费项目": "酒店", "消费类型": "住宿", "总金额": 600, "付款人": "小红", "平摊人数": 3, "平摊成员": ["小明", "小红", "小华"]}},
            {"fields": {"消费项目": "晚餐", "消费类型": "餐饮", "总金额": 300, "付款人": "小华", "平摊人数": 2, "平摊成员": ["小明", "小红"]}},
            {"fields": {"消费项目": "加油", "消费类型": "交通", "总金额": 100, "付款人": "小明", "平摊人数": 3, "平摊成员": ["小明", "小红", "小华"]}},
            {"fields": {"消费项目": "景点门票", "消费类型": "门票/娱乐", "总金额": 150, "付款人": "小红", "平摊人数": 2, "平摊成员": ["小明", "小华"]}},
        ]
        records = mock_records
    else:
        # 从飞书读取
        records = read_feishu_table(args.app_token, args.table)
        if not records:
            print("无法读取飞书数据，请检查授权")
            return
    
    if not records:
        print("📭 暂无消费记录")
        return
    
    balances, stats, total = calculate_balances(records, {})
    transfers = calculate_optimal_transfers(balances)
    
    print(format_report(balances, stats, total, transfers))
    
    # 输出 JSON 格式（供其他程序使用）
    output = {
        "total": total,
        "balances": balances,
        "stats": stats,
        "transfers": [{"from": f, "to": t, "amount": a} for f, t, a in transfers]
    }
    print("\n\n📋 JSON 输出:")
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
