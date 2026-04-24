--- 
name: skill-astrbot-dev
description: Reference + workflow notes for AstrBot plugin development (messages, platform adapters, plugin config, agent system).
metadata: 
  short-description: AstrBot dev reference
---

# skill-astrbot-dev

这是 AstrBot 开发者文档的权威索引。选择此技能时，立即基于最少必需的文档+代码入口点，避免重复阅读，始终以代码为最终权威。

## 使用时机

当你需要以下帮助时使用此技能：
- AstrBot 插件结构、装饰器/钩子、生命周期、模式、会话
- 消息模型/事件流和消息链转换
- 平台适配器接口和消息转换模式
- 代理相关主题（工具/提供者/角色/子代理/沙盒/定时任务/上下文压缩）

## 强制性工作流程（每次都要使用）

1. **从单个入口点开始**（避免广泛加载）：
   - 站点索引：`docs/index.md`
   - 核心概念：`docs/design_standards/core_concepts.md`

2. **选择一个主题文件夹并保持专注**：
   - 代理系统：`docs/agent/`
   - 插件配置：`docs/plugin_config/`
   - 消息：`docs/messages/`
   - 平台适配器：`docs/platform_adapters/`

3. **如果用户针对特定 AstrBot 版本，交叉检查**：
   - `docs/snapshots/<version>/`

4. **如果文档和代码不一致，以代码为准**：
   - 核心代码位于 `astrbotcore/astrbot/core/`（只读取需要的文件）

## 强烈建议：编写插件时使用 AstrBot SDK

编写插件代码时，强烈建议在本地安装 AstrBot SDK，用于 API 参考、签名查找和 IDE 自动完成。

```powershell
python -m pip install -U astrbot
```

在实现钩子、提供者/上下文调用和代理运行器集成时，优先使用 SDK 符号。这有助于减少猜测和签名不匹配。

如果此仓库中的 AstrBot 源代码可用，仍应将仓库代码视为比包文档更高的优先级。

## 插件项目结构（强烈建议）

标准的 AstrBot 插件项目应包括：
- `main.py`：入口点。在此实现插件启动和主要功能
- `metadata.yaml`：插件元数据（名称、版本、作者、仓库、描述）
- `README.md`：安装、使用、功能概述和开发链接
- `.gitignore`：忽略 Python 缓存和 IDE 配置文件
- `LICENSE`：开源许可证文件

## `metadata.yaml` 最小模板

```yaml
name: astrbot_plugin_helloworld # 插件唯一识别名，最好以 astrbot_plugin_ 前缀开头
display_name: helloworld # 展示名（v4.5.0+）
desc: AstrBot 插件示例。 # 插件简短描述
version: v1.3.0 # 版本号：v1.1.1 或 v1.1
author: Soulter # 作者
repo: https://github.com/Soulter/helloworld # 插件的仓库地址
```

## 插件实现的代码规则

- 对处理程序/钩子/工具函数使用 `async def`
- 保持 `main.py` 专注于插件入口和编排；将复杂逻辑提取到子模块中
- 为公共方法和钩子签名添加类型提示
- 不要硬编码提供者 ID 或密钥；在 `_conf_schema.json` 中公开可配置字段
- 偏好小型、可测试的函数，而不是大型单一处理程序体
- 保持 README 和元数据与实际插件行为和版本一致
- 如果你编写的是 AstrBot 核心代码而不是插件，如果更改需要文档更新，必须向 https://github.com/AstrBotDevs/AstrBot-docs 提交 PR

## 钩子：避免缺失/过时的引用

有两个不同的"钩子"层不能混淆：
- 插件事件钩子（装饰器）：`docs/plugin_config/hooks.md`
- 代理运行器钩子（`BaseAgentRunHooks`）：`docs/agent/agent-related-hooks.md`

如果需要完整的钩子清单（因为上下文可能被截断），请在本地生成：
```powershell
python scripts/generate_hook_inventory.py
```

这将写入 `docs/.tmp/hook_inventory/`（gitignored）。将其用作编写/更新文档的草稿纸；不要将 `.tmp` 路径引用为公共文档 URL。

## 高信号代码入口点（仅在需要时打开）

- 事件钩子注册+签名：`astrbotcore/astrbot/core/star/register/star_handler.py`
- 事件类型：`astrbotcore/astrbot/core/star/star_handler.py`
- 代理运行器+钩子调用顺序：`astrbotcore/astrbot/core/agent/runners/`
- 代理钩子接口：`astrbotcore/astrbot/core/agent/hooks.py`
- 主代理构建（沙盒/定时任务/工具）：`astrbotcore/astrbot/core/astr_main_agent.py`
- 技能系统（AstrBot 运行时技能）：`astrbotcore/astrbot/core/skills/skill_manager.py`
- 子代理配置加载：`astrbotcore/astrbot/core/subagent_orchestrator.py`
