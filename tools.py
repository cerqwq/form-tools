"""
Form Tools - AI表单工具
支持表单生成、验证、处理
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class FormTools:
    """
    AI表单工具
    支持：生成、验证、处理
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def generate_form(self, purpose: str, fields: List[str] = None) -> str:
        """生成表单"""
        if not self.client:
            return "LLM客户端未配置"

        fields_text = "\n".join(f"- {f}" for f in (fields or []))

        prompt = f"""请为{purpose}生成HTML表单：

{f'字段：{fields_text}' if fields_text else ''}

要求：
1. 响应式设计
2. 表单验证
3. 美观样式
4. 可直接使用"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_form_schema(self, purpose: str) -> Dict:
        """生成表单Schema"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{purpose}生成JSON Schema表单定义：

请返回JSON格式：
{{
    "title": "表单标题",
    "fields": [
        {{
            "name": "字段名",
            "type": "类型",
            "label": "标签",
            "required": true/false,
            "validation": {{}},
            "placeholder": "占位符"
        }}
    ]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"schema": content}

    def generate_validation(self, schema: Dict, framework: str = "pydantic") -> str:
        """生成验证代码"""
        if not self.client:
            return "LLM客户端未配置"

        schema_text = json.dumps(schema, ensure_ascii=False)

        prompt = f"""请根据以下Schema生成{framework}验证代码：

{schema_text}

要求：
1. 完整的验证逻辑
2. 错误消息
3. 类型提示"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_survey(self, topic: str, question_count: int = 10) -> Dict:
        """生成调查问卷"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{topic}生成{question_count}道调查问卷：

请返回JSON格式：
{{
    "title": "问卷标题",
    "description": "问卷描述",
    "questions": [
        {{
            "id": 1,
            "type": "单选/多选/文本/评分",
            "question": "问题",
            "options": ["选项1", "选项2"],
            "required": true/false
        }}
    ]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"survey": content}

    def analyze_responses(self, responses: List[Dict]) -> Dict:
        """分析问卷结果"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        responses_text = json.dumps(responses[:20], ensure_ascii=False)

        prompt = f"""请分析以下问卷结果：

{responses_text}

请返回JSON格式：
{{
    "summary": "总结",
    "insights": ["洞察1", "洞察2"],
    "statistics": {{"key": "value"}},
    "recommendations": ["建议1", "建议2"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"analysis": content}


def create_tools(**kwargs) -> FormTools:
    """创建表单工具"""
    return FormTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("Form Tools")
    print()

    # 测试
    schema = tools.generate_form_schema("用户注册")
    print(json.dumps(schema, ensure_ascii=False, indent=2))
