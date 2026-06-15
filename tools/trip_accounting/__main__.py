#!/usr/bin/env python3
"""
旅行记账 - 飞书交互入口
整合所有功能，提供统一的飞书交互界面
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from add_flow import AddState, format_question_card, format_confirmation, QUESTIONS, CONSUMPTION_TYPES
from trip_accounting import calculate_balances, calculate_optimal_transfers, format_report

# 飞书配置
BITABLE_APP_TOKEN = "IzDTbaKqcaO8jfsvzk8caCNangi"
CONSUMPTION_TABLE_ID = "tblnD6bpJAllpodn"

# 全局状态
_state = AddState.load()


def start_add(user_id: str) -> str:
    """开始添加消费记录"""
    result = _state.start(user_id)
    return format_question_card(result)


def answer_add(user_id: str, answer: str) -> str:
    """回答添加问题"""
    result = _state.answer(user_id, answer)
    
    if "error" in result:
        return f"❌ {result['error']}"
    
    if result.get("done"):
        return format_confirmation(result["record"])
    
    return format_question_card(result)


def get_stats_message(records: list) -> str:
    """获取统计消息"""
    if not records:
        return "📭 暂无消费记录，快来添加第一笔吧！\n\n发送 /add 开始添加消费记录"
    
    balances, stats, total = calculate_balances(records, {})
    transfers = calculate_optimal_transfers(balances)
    return format_report(balances, stats, total, transfers)


def get_help_message() -> str:
    """获取帮助信息"""
    return """
📖 **旅行记账命令**

**添加消费（问卷模式）**
```
/add
```
引导你一步步填写消费记录

**添加消费（快捷命令）**
```
/add 项目 类型 金额 付款人 平摊人数 [平摊成员]
```
示例：`/add 晚餐 餐饮 300 小明 3 小明,小红,小华`

**查看统计**
```
/stats
```
显示总消费、每人消费、净余额、最优转账方案

**一键平账**
```
/settle
```
只显示最优转账方案

**成员管理**
```
/addmember 小明
/delmember 小明
```

---
💡 消费类型：餐饮、交通、住宿、门票/娱乐、购物、其他
💡 平摊成员用逗号分隔，留空按人数平摊
""".strip()


def cancel_add(user_id: str) -> str:
    """取消添加"""
    global _state
    _state.reset()
    return "❌ 已取消添加消费记录"


# 测试
if __name__ == "__main__":
    print("=== 测试帮助 ===")
    print(get_help_message())
    print()
    print("=== 测试添加流程 ===")
    state = AddState()
    result = state.start("test")
    print(format_question_card(result))
