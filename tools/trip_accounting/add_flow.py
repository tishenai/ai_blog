#!/usr/bin/env python3
"""
旅行记账 - 问卷式添加消费流程
通过飞书交互式问题引导用户填写消费记录

工作流程:
1. 用户发送 /add 或点击按钮
2. Bot 依次询问: 项目 → 类型 → 金额 → 付款人 → 平摊人数 → 平摊成员
3. Bot 将记录写入飞书多维表格
"""

import sys
import os
import json
from typing import List, Dict, Optional

# 配置文件路径
CONFIG_DIR = os.path.expanduser("~/.openclaw/workspace/ai_blog/tools/trip_accounting")
STATE_FILE = os.path.join(CONFIG_DIR, "add_state.json")

# 飞书配置
BITABLE_APP_TOKEN = "IzDTbaKqcaO8jfsvzk8caCNangi"
CONSUMPTION_TABLE_ID = "tblnD6bpJAllpodn"

# 字段ID
FIELD_IDS = {
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

# 消费类型选项
CONSUMPTION_TYPES = ["餐饮", "交通", "住宿", "门票/娱乐", "购物", "其他"]

def get_type_desc(t: str) -> str:
    """获取消费类型描述"""
    descs = {
        "餐饮": "吃饭、下午茶等",
        "交通": "机票、高铁、打车等",
        "住宿": "酒店、民宿等",
        "门票/娱乐": "景点门票、电影、KTV等",
        "购物": "买纪念品、特产等",
        "其他": "其他消费"
    }
    return descs.get(t, "")

# 问题列表（顺序）
QUESTIONS = [
    {
        "header": "消费项目",
        "question": "这是什么消费？（如：晚餐、机票、酒店）",
        "field": "消费项目",
        "type": "text",
        "options": []
    },
    {
        "header": "消费类型",
        "question": "这是什么类型的消费？",
        "field": "消费类型",
        "type": "select",
        "options": [
            {"label": t, "description": get_type_desc(t)} for t in CONSUMPTION_TYPES
        ]
    },
    {
        "header": "总金额",
        "question": "消费总金额是多少？（单位：元）",
        "field": "总金额",
        "type": "text",
        "options": []
    },
    {
        "header": "付款人",
        "question": "谁付的钱？（输入成员名字）",
        "field": "付款人",
        "type": "text",
        "options": []
    },
    {
        "header": "平摊人数",
        "question": "有几个人平摊这笔钱？",
        "field": "平摊人数",
        "type": "text",
        "options": []
    },
    {
        "header": "平摊成员",
        "question": "哪几个人平摊？（用逗号分隔，如：小明,小红,小华）\n留空表示按人数自动平摊",
        "field": "平摊成员",
        "type": "text",
        "options": []
    },
]


def get_type_desc(t: str) -> str:
    """获取消费类型描述"""
    descs = {
        "餐饮": "吃饭、下午茶等",
        "交通": "机票、高铁、打车等",
        "住宿": "酒店、民宿等",
        "门票/娱乐": "景点门票、电影、KTV等",
        "购物": "买纪念品、特产等",
        "其他": "其他消费"
    }
    return descs.get(t, "")


class AddState:
    """管理添加消费的状态"""
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        """重置状态"""
        self.active = False
        self.answers = {}
        self.current_step = 0
        self.user_id = None
    
    def start(self, user_id: str) -> Dict:
        """开始新的添加流程"""
        self.reset()
        self.active = True
        self.user_id = user_id
        self.answers = {}
        self.current_step = 0
        self._save()
        return self._get_current_question()
    
    def answer(self, user_id: str, answer: str) -> Dict:
        """回答当前问题"""
        if not self.active or self.user_id != user_id:
            return {"error": "没有正在进行的添加流程，请先发送 /add 开始"}
        
        question = QUESTIONS[self.current_step]
        field = question["field"]
        
        # 特殊处理
        if field == "总金额":
            try:
                float(answer)
            except ValueError:
                return {"error": f"金额必须是数字，当前值：{answer}"}
        elif field == "平摊人数":
            try:
                int(answer)
            except ValueError:
                return {"error": f"平摊人数必须是数字，当前值：{answer}"}
        
        self.answers[field] = answer
        self.current_step += 1
        self._save()
        
        if self.current_step >= len(QUESTIONS):
            return self._finish()
        
        return self._get_current_question()
    
    def _get_current_question(self) -> Dict:
        """获取当前问题"""
        q = QUESTIONS[self.current_step]
        return {
            "step": self.current_step + 1,
            "total": len(QUESTIONS),
            "header": q["header"],
            "question": q["question"],
            "field": q["field"],
            "type": q["type"],
            "options": q["options"]
        }
    
    def _finish(self) -> Dict:
        """完成所有问题"""
        self.active = False
        
        # 计算人均金额
        amount = float(self.answers.get("总金额", 0))
        split_members = self.answers.get("平摊成员", "")
        split_count = int(self.answers.get("平摊人数", 1))
        
        if split_members:
            members_list = [m.strip() for m in split_members.split(",") if m.strip()]
            per_person = round(amount / len(members_list), 2)
        elif split_count > 0:
            per_person = round(amount / split_count, 2)
        else:
            per_person = amount
        
        self.answers["人均金额"] = per_person
        self.answers["结算状态"] = "待结算"
        
        result = {"done": True, "record": self.answers.copy()}
        self._save()
        return result
    
    def _save(self):
        """保存状态到文件"""
        os.makedirs(CONFIG_DIR, exist_ok=True)
        state = {
            "active": self.active,
            "answers": self.answers,
            "current_step": self.current_step,
            "user_id": self.user_id
        }
        with open(STATE_FILE, "w") as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
    
    @classmethod
    def load(cls) -> "AddState":
        """从文件加载状态"""
        state = cls()
        if os.path.exists(STATE_FILE):
            try:
                with open(STATE_FILE, "r") as f:
                    data = json.load(f)
                state.active = data.get("active", False)
                state.answers = data.get("answers", {})
                state.current_step = data.get("current_step", 0)
                state.user_id = data.get("user_id")
            except:
                pass
        return state


def format_question_card(question: Dict) -> str:
    """格式化问题为卡片文本"""
    step = question["step"]
    total = question["total"]
    header = question["header"]
    text = question["question"]
    
    msg = f"""
📝 **添加消费记录** ({step}/{total})

**{header}**
{text}

💡 输入你的回答即可继续
"""
    return msg.strip()


def format_confirmation(record: Dict) -> str:
    """格式化确认信息"""
    split_members = record.get("平摊成员", "")
    if split_members:
        members_list = [m.strip() for m in split_members.split(",") if m.strip()]
        split_text = f"{', '.join(members_list)} ({len(members_list)}人)"
    else:
        split_text = f"{record.get('平摊人数', 1)}人平摊"
    
    msg = f"""
✅ **消费记录已确认！**

| 项目 | 内容 |
|------|------|
| 📝 消费项目 | {record.get('消费项目')} |
| 🏷️ 消费类型 | {record.get('消费类型')} |
| 💰 总金额 | ¥{float(record.get('总金额', 0)):.2f} |
| 👤 付款人 | {record.get('付款人')} |
| 👥 平摊 | {split_text} |
| 💵 人均 | ¥{float(record.get('人均金额', 0)):.2f} |

已自动写入飞书表格 ✨
"""
    return msg.strip()


if __name__ == "__main__":
    # 测试状态机
    state = AddState()
    
    print("=== 测试问卷流程 ===\n")
    
    # 模拟开始
    result = state.start("test_user")
    print(format_question_card(result))
    print()
    
    # 模拟回答
    answers = ["晚餐", "餐饮", "300", "小明", "3", "小明,小红,小华"]
    for ans in answers:
        result = state.answer("test_user", ans)
        if result.get("done"):
            print(format_confirmation(result["record"]))
        else:
            print(format_question_card(result))
            print()
