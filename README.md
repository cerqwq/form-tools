# 📋 Form Tools

AI表单工具，支持表单生成、验证、处理。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 📝 表单HTML生成
- 📊 表单Schema生成
- ✅ 验证代码生成
- 📋 调查问卷生成
- 📈 问卷结果分析

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from form_tools import create_tools

tools = create_tools()

# 生成表单
form = tools.generate_form("用户注册", ["用户名", "邮箱", "密码"])

# 生成Schema
schema = tools.generate_form_schema("用户注册")

# 生成验证代码
validation = tools.generate_validation(schema, "pydantic")

# 生成调查问卷
survey = tools.generate_survey("用户满意度", 10)

# 分析结果
analysis = tools.analyze_responses(responses)
```

## 📁 项目结构

```
form-tools/
├── tools.py       # 表单工具核心
└── README.md
```

## 📄 许可证

MIT License
