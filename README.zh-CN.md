# OneChartLab Slides

[English](README.md) | **简体中文**

> 面向 AI Agent 的 HTML 幻灯片制作系统。你提供材料和要求，Agent 负责把它做成可播放、可继续修改的演示文稿。

OneChartLab Slides 为 AI Agent 提供了一套明确的设计规范、16 种常用版式和完整的 ZXcharT 深色视觉主题。它的重点不是让用户亲自编写 HTML，而是让 Agent 在统一的视觉与结构约束下，稳定地生成质量更高的演示文稿。

用户主要通过自然语言与 Agent 沟通。HTML 是 Agent 生成的交付格式，不是用户必须掌握的操作方式。

## 它解决什么问题

通用 AI 虽然可以生成网页，但制作演示文稿时常见这些问题：页面风格不统一、内容层级混乱、信息密度失控、每一页都像临时拼出来的。

OneChartLab Slides 为 Agent 提供：

- 统一的字体、颜色、间距和动效规范
- 16 种适用于不同内容目的的页面结构
- 可直接复制和改写的 HTML 模板
- 从内容规划、生成到预览检查的工作流程
- 可继续修改、可以直接用浏览器播放的最终文件

## 哪些 Agent 可以使用

任何能够读取和写入本地文件的 AI Agent 都可以使用。若 Agent 还能打开或预览 HTML，就可以进一步检查文字溢出、页面比例、交互和可读性。

使用时可以：

- 将本仓库文件夹提供给 Agent；或
- 将本仓库安装为 Agent Skill；或
- 让 Agent 读取仓库中的 `SKILL.md`、`AGENTS.md` 和主题规范。

项目不绑定特定模型或特定 Agent 平台。

## 安装 Skill

请安装完整的 **`onechartlab-slides` 文件夹**，不要只复制 `SKILL.md`。模板、设计规范、版式说明和脚本也是 Skill 的组成部分。使用 ZIP 上传时，压缩包内应只有一个顶层文件夹，并且名称必须是 `onechartlab-slides/`。

### HanaAgent

可以直接让 HanaAgent 从 GitHub 安装，或在 Skill 安装界面选择仓库/ZIP：

```text
请安装这个 Skill：https://github.com/ZXcharT/onechartlab-slides
```

需要手动放置文件夹时，参见 [docs/platforms/hanaagent.md](docs/platforms/hanaagent.md)。

### Claude

先启用 **Code execution and file creation**，然后进入 **Customize → Skills → Add/Create skill → Upload a skill**，上传内部顶层文件夹为 `onechartlab-slides/` 的 ZIP。

### OpenAI Codex

可以让 `$skill-installer` 从 GitHub 仓库安装，也可以把完整文件夹放到：

```text
~/.agents/skills/onechartlab-slides/
```

只想在某个项目中使用时，放到该项目的 `.agents/skills/onechartlab-slides/`。如果新安装的 Skill 没有出现，重启 Codex。

### 第一次调用

安装后可以直接描述需求，也可以在支持显式选择 Skill 的 Agent 中主动指定它：

```text
请使用 OneChartLab Slides，把这份报告制作成 10 页演示文稿。
先给我页面大纲，确认后再生成 HTML。
```

## 用 Agent 制作演示文稿

### 1. 让 Agent 读取规则

可以先对 Agent 说：

```text
请先阅读 OneChartLab Slides 仓库中的 SKILL.md、AGENTS.md
和 themes/zxchart/design.md，后续使用这套系统制作演示文稿。
```

### 2. 提供制作简报

至少说明主题、受众、目标和材料。需要时再补充页数、语气和视觉要求。

```text
请使用 OneChartLab Slides 制作一份 12 页演示文稿。
主题：AI 基础设施投资周期
受众：个人投资者
目标：解释产业链的核心瓶颈和验证信号
材料：使用我提供的研究文档
要求：先给出页面大纲，确认后再生成 HTML；所有数据注明来源。
```

### 3. 确认页面大纲

Agent 会根据内容目的选择合适的版式。建议先确认每页讲什么，再让它生成完整文件，避免排版完成后大幅调整叙事结构。

### 4. 生成并检查

一个完整流程通常包括：

1. 阅读材料，提炼核心结论；
2. 规划页面顺序并选择版式；
3. 复制 `template.html` 创建项目；
4. 写入标题、正文、数据和来源；
5. 在浏览器中预览；
6. 检查事实、链接、文字溢出和页面可读性；
7. 根据反馈继续修改。

更完整的执行与验证规范参见 [AGENTS.md](AGENTS.md) 和 [SKILL.md](SKILL.md)。

## 需要会 HTML 吗？

**不需要会 HTML。** 普通用户只需要通过自然语言告诉 Agent 想做什么，并对大纲和最终效果做判断。

生成后的演示文稿以 HTML 文件交付，可以直接用浏览器播放。如果你熟悉 HTML/CSS，也可以在 Agent 生成后进行精细调整，但这不是主要使用方式。

## 内置版式

- **开场与收尾**：`layout-cover`、`layout-outro`、`layout-closing`
- **目录与内容结构**：`layout-agenda`、`layout-split`、`layout-detail`、`layout-stack`
- **数据与比较**：`layout-metrics`、`layout-dashboard`、`layout-bars`、`layout-compare`
- **叙事与观点**：`layout-quote`、`layout-timeline`、`layout-timeline-3col`、`layout-hook`、`layout-statement`

Agent 会根据每页的表达目的选择版式，而不是让用户自己记住这些名称。详细说明参见 [docs/layouts.md](docs/layouts.md)。

## 主要特点

- 16 种常用版式，覆盖封面、目录、数据、对比、时间轴、观点和收尾等场景
- 单个 HTML 文件承载主要内容、样式和交互，便于交付与继续修改
- 采用 ZXcharT 深色主题，以金色作为重点强调色
- 支持键盘、触控和页面按钮切换幻灯片
- 支持卡片聚焦、条形图动画和减少动态效果的系统设置
- 不绑定特定 AI 平台，也不依赖私有金融工具或个人环境

## 关键文件

```text
.
├── SKILL.md                       Agent 使用入口和任务说明
├── AGENTS.md                      制作、检查和协作流程
├── template.html                  Agent 创建演示文稿时使用的基础模板
├── index.html                     16 种版式的预览入口
├── themes/zxchart/design.md       视觉规范与版式清单
├── docs/                          布局、定制和平台使用说明
├── examples/agent-workflow/       通用 Agent 工作流示例
├── scripts/                       Agent 或高级用户可调用的项目脚本
├── projects/                      新生成的演示文稿默认保存在这里
└── assets/                        项目使用的图片等素材
```

## 高级用法：手动创建项目

这不是普通用户的主要使用方式。熟悉命令行或 HTML 的用户，可以手动复制 `template.html`，也可以使用脚本创建项目目录。

### macOS / Linux

```sh
sh scripts/new-project.sh "my-deck"
```

### Windows

```powershell
py scripts/new-project.py "my-deck"
```

脚本只会在 `projects/my-deck/` 中创建一份模板副本，不会上传文件或连接 AI 服务。Agent 也可以在执行任务时自行调用这些脚本。

## 浏览器兼容性

建议使用当前版本的 Chrome、Edge、Firefox 或 Safari。页面中的 JavaScript 用于切换幻灯片和部分交互；即使无法加载 Google Fonts，也会自动使用系统字体。

## 致谢

模板基础来自 Zara Zhang 的 [beautiful-html-templates](https://github.com/zarazhangrui/beautiful-html-templates)，采用 MIT 许可证。[frontend-slides](https://github.com/zarazhangrui/frontend-slides) 和 [html-presentation](https://github.com/juanjuanjie/html-presentation) 为工作流与演示方法提供了参考。详情参见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) 和 [SOURCES.md](SOURCES.md)。

## 许可证与商标

代码、文档和通用示例采用 [MIT 许可证](LICENSE)。OneChartLab、OneChartLab Slides、ZXcharT 名称及其 Logo 的相关权利保留，详见 [TRADEMARKS.md](TRADEMARKS.md)。
