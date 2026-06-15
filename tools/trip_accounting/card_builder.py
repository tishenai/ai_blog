#!/usr/bin/env python3
"""
旅行记账 - 交互式消费记录卡片生成
生成飞书消息卡片 JSON，用于添加消费记录
"""

import json
from typing import Dict, List, Optional

# 消费类型选项
CONSUMPTION_TYPES = [
    {"label": "🍜 餐饮", "value": "餐饮"},
    {"label": "🚗 交通", "value": "交通"},
    {"label": "🏨 住宿", "value": "住宿"},
    {"label": "🎫 门票/娱乐", "value": "门票/娱乐"},
    {"label": "🛍️ 购物", "value": "购物"},
    {"label": "📦 其他", "value": "其他"},
]

# 结算状态
SETTLEMENT_STATUS = [
    {"label": "⏳ 待结算", "value": "待结算"},
    {"label": "✅ 已结算", "value": "已结算"},
]


def build_add_record_card(members: List[str] = None) -> Dict:
    """
    生成添加消费记录的交互卡片
    这是一个飞书 Interactive 消息卡片
    """
    member_options = []
    if members:
        for m in members:
            member_options.append({"text": {"tag": "plain_text", "content": m}, "value": m})
    
    elements = [
        {
            "tag": "div",
            "text": {
                "tag": "lark_md",
                "content": "**📝 添加消费记录**\n\n请填写以下信息："
            }
        },
        {"tag": "hr"},
        {
            "tag": "div",
            "text": {"tag": "plain_text", "content": "消费项目（如：晚餐、机票、酒店）"}
        },
        {
            "tag": "input",
            "name": "project",
            "placeholder": {"tag": "plain_text", "content": "请输入消费项目"},
            "action_type": "input"
        },
        {"tag": "div", "text": {"tag": "plain_text", "content": "消费类型"}},
        {
            "tag": "select_static",
            "name": "category",
            "options": CONSUMPTION_TYPES
        },
        {"tag": "div", "text": {"tag": "plain_text", "content": "总金额（元）"}},
        {
            "tag": "input",
            "name": "amount",
            "placeholder": {"tag": "plain_text", "content": "请输入金额，如 300"},
            "action_type": "input_number"
        },
        {"tag": "div", "text": {"tag": "plain_text", "content": "付款人"}},
        {
            "tag": "select_static",
            "name": "payer",
            "options": [{"label": {"tag": "plain_text", "content": m}, "value": m} for m in (members or ["小明", "小红", "小华"])]
        },
    ]
    
    if member_options:
        elements.extend([
            {"tag": "div", "text": {"tag": "plain_text", "content": "平摊成员（可多选）"}},
            {
                "tag": "select_person",
                "name": "split_members",
                "options": member_options
            },
        ])
    
    elements.extend([
        {"tag": "hr"},
        {
            "tag": "action",
            "actions": [
                {
                    "tag": "button",
                    "text": {"tag": "lark_md", "content": "**✅ 确认添加**"},
                    "type": "primary",
                    "action_type": "submit"
                },
                {
                    "tag": "button",
                    "text": {"tag": "lark_md", "content": "取消"},
                    "type": "default",
                    "action_type": "cancel"
                }
            ]
        }
    ])
    
    return {
        "schema": "interactive",
        "body": {
            "tag": "card",
            "children": elements
        }
    }


def build_stats_card(balances: Dict, stats: Dict, total: float, transfers: List) -> Dict:
    """生成统计报告卡片"""
    
    # 每人明细
    member_details = []
    for member, s in sorted(stats.items(), key=lambda x: -x[1]["paid"]):
        diff = s["paid"] - s["share"]
        diff_str = f"+¥{diff:.2f}" if diff >= 0 else f"-¥{abs(diff):.2f}"
        emoji = "📈" if diff > 0 else "📉" if diff < 0 else "⚖️"
        member_details.append({
            "tag": "div",
            "text": {
                "tag": "lark_md",
                "content": f"**{member}**\n已付 ¥{s['paid']:.2f} | 应摊 ¥{s['share']:.2f} | 差额 {emoji} {diff_str}"
            }
        })
    
    # 转账方案
    transfer_details = []
    if transfers:
        for i, (from_p, to_p, amount) in enumerate(transfers, 1):
            transfer_details.append({
                "tag": "div",
                "text": {
                    "tag": "lark_md",
                    "content": f"**{i}.** {from_p} → {to_p}: ¥{amount:.2f}"
                }
            })
    else:
        transfer_details.append({
            "tag": "div",
            "text": {"tag": "lark_md", "content": "✅ 所有账目已结清！"}
        })
    
    card = {
        "schema": "interactive",
        "body": {
            "tag": "card",
            "children": [
                {"tag": "div", "text": {"tag": "lark_md", "content": "## 🧾 旅行记账统计报告"}},
                {"tag": "hr"},
                {"tag": "div", "text": {"tag": "lark_md", "content": f"### 💰 总消费：¥{total:.2f}"}},
                {"tag": "hr"},
                {"tag": "div", "text": {"tag": "lark_md", "content": "### 📊 每人消费明细"}},
                *member_details,
                {"tag": "hr"},
                {"tag": "div", "text": {"tag": "lark_md", "content": "### 🔄 最优转账方案"}},
                *transfer_details,
            ]
        }
    }
    
    return card


def parse_card_response(response: Dict) -> Dict:
    """解析卡片返回的数据"""
    values = response.get("value", {})
    return {
        "project": values.get("project", ""),
        "category": values.get("category", ""),
        "amount": values.get("amount", 0),
        "payer": values.get("payer", ""),
        "split_members": values.get("split_members", [])
    }


if __name__ == "__main__":
    # 测试生成卡片
    card = build_add_record_card(["小明", "小红", "小华"])
    print(json.dumps(card, ensure_ascii=False, indent=2))
