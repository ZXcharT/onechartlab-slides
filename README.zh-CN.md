# OneChartLab Slides

[English](README.md) | **简体中文**

> 一套可以直接在浏览器中运行的 HTML 幻灯片模板。既可以手动制作，也可以交给 AI Agent 生成。

OneChartLab Slides 内置 16 种常用版式和一套完整的 ZXcharT 深色视觉主题，适合制作研究报告、方案汇报、数据展示和视频分镜。每份演示文稿以一个 HTML 文件为主体，不需要安装专用演示软件，也不依赖前端工程环境，使用浏览器即可打开和播放。

## 它适合做什么

- 将研究文章或报告整理成结构清晰的演示文稿
- 制作数据看板、指标对比、时间轴和观点页
- 为视频内容设计画面结构与分镜
- 快速搭建风格统一的项目汇报或产品介绍
- 让 AI Agent 根据材料生成可继续编辑的 HTML Slides

## 主要特点

- 16 种常用版式，覆盖封面、目录、数据、对比、时间轴、观点和收尾等场景
- 单个 HTML 文件即可保存主要内容、样式和交互，便于复制、修改与分享
- 采用 ZXcharT 深色主题，以金色作为重点强调色
- 支持键盘、触控和页面按钮切换幻灯片
- 支持卡片聚焦、条形图动画和减少动态效果的系统设置
- 不绑定特定 AI 平台，也不要求使用任何私有工具

## 是否必须使用 AI Agent？

**不需要。** OneChartLab Slides 本身就是一套普通的 HTML 模板，没有 Agent 也可以独立使用。

| 使用方式 | 怎么用 | 适合谁 |
|---|---|---|
| 直接修改模板 | 复制 `template.html`，使用文本或代码编辑器替换内容 | 熟悉一点 HTML，想完全手动控制内容的人 |
| 使用生成脚本 | 运行一条命令，自动创建新的项目文件夹和模板副本 | 想快速开始并保持项目目录整洁的人 |
| 交给 AI Agent | 提供材料、受众和页数，让 Agent 生成并检查演示文稿 | 想提高整理与排版效率的人 |

三种方式生成的是同一种 HTML 演示文稿，可以自由切换，也可以先让 Agent 生成，再手动修改。

## 最快体验

无需安装依赖，也无需使用 AI Agent：

1. 下载或克隆本仓库。
2. 双击打开 `index.html`，浏览全部版式和交互效果。
3. 复制一份 `template.html`，例如重命名为 `my-deck.html`。
4. 使用任意文本或代码编辑器修改标题、正文、数据和页面顺序。
5. 用浏览器打开修改后的文件，刷新页面即可查看效果。

如果只是想先看看它长什么样，完成前两步就够了。

## 可选：用脚本创建新项目

生成脚本只是一个“复制模板”的快捷工具。它会在 `projects/` 下新建文件夹，并把 `template.html` 复制为该项目的 `index.html`。脚本不会上传文件、不会连接 AI 服务，也不会修改原模板。

### macOS / Linux

```sh
sh scripts/new-project.sh "my-deck"
```

生成结果：

```text
projects/my-deck/index.html
```

### Windows

```powershell
py scripts/new-project.py "my-deck"
```

生成完成后，用浏览器打开 `projects/my-deck/index.html`，再使用编辑器修改其中的内容即可。macOS/Linux 用户使用 Shell 脚本时不需要安装 Python；Windows 示例需要本机已安装 Python 3。

## 可选：与 AI Agent 配合使用

你可以把仓库目录、参考材料和制作要求交给支持文件编辑的 AI Agent，例如：

```text
请使用 OneChartLab Slides 制作一份 12 页演示文稿。
受众：个人投资者
目标：解释某个产业趋势
要求：先给出页面大纲，确认后再生成 HTML；所有数据注明来源。
```

一个稳妥的制作流程是：

1. 明确受众、目标、页数和视觉要求；
2. 从 16 种版式中选择合适的页面结构；
3. 确认大纲后复制 `template.html`；
4. 写入内容并预览；
5. 检查事实、链接、文字溢出和页面可读性；
6. 根据反馈继续修改。

更完整的 Agent 操作说明参见 [AGENTS.md](AGENTS.md) 和 [SKILL.md](SKILL.md)。

## 内置版式

- **开场与收尾**：`layout-cover`、`layout-outro`、`layout-closing`
- **目录与内容结构**：`layout-agenda`、`layout-split`、`layout-detail`、`layout-stack`
- **数据与比较**：`layout-metrics`、`layout-dashboard`、`layout-bars`、`layout-compare`
- **叙事与观点**：`layout-quote`、`layout-timeline`、`layout-timeline-3col`、`layout-hook`、`layout-statement`

各版式的详细用途与限制参见 [docs/layouts.md](docs/layouts.md)。

## 关键文件

```text
.
├── index.html                    版式预览入口，下载后可直接打开
├── template.html                 制作新演示文稿时使用的基础模板
├── themes/zxchart/design.md      主题规范与版式清单
├── docs/                         布局、定制和平台使用说明
├── examples/agent-workflow/      通用 Agent 工作流示例
├── scripts/                      可选的项目生成脚本和仓库检查器
├── projects/                     脚本生成的新项目默认保存在这里
└── assets/                       可自行放置图片等素材
```

## 修改主题

复制模板后，可以在 HTML 文件的 `:root` 区域修改背景色、强调色、正文色和边框色等 CSS 变量。建议保持足够的文字对比度，并检查小屏幕和减少动态效果设置下的显示效果。详细说明参见 [docs/customization.md](docs/customization.md)。

## 浏览器兼容性

建议使用当前版本的 Chrome、Edge、Firefox 或 Safari。页面中的 JavaScript 用于切换幻灯片和部分交互；即使无法加载 Google Fonts，也会自动使用系统字体。

## 致谢

模板基础来自 Zara Zhang 的 [beautiful-html-templates](https://github.com/zarazhangrui/beautiful-html-templates)，采用 MIT 许可证。[frontend-slides](https://github.com/zarazhangrui/frontend-slides) 和 [html-presentation](https://github.com/juanjuanjie/html-presentation) 为工作流与演示方法提供了参考。详情参见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) 和 [SOURCES.md](SOURCES.md)。

## 许可证与商标

代码、文档和通用示例采用 [MIT 许可证](LICENSE)。OneChartLab、OneChartLab Slides、ZXcharT 名称及其 Logo 的相关权利保留，详见 [TRADEMARKS.md](TRADEMARKS.md)。
