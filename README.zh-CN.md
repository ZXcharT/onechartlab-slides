# OneChartLab Slides

[English](README.md) | **简体中文**

OneChartLab Slides v0.1.0 是一套面向 AI Agent 的 HTML 演示文稿系统，也是 ZXcharT 旗下 OneChartLab 开源生态中的独立项目。它提供采用 ZXcharT 视觉主题、可移植的单文件幻灯片模板；本仓库不是 OneChartLab 品牌总入口，也不是网站源码仓库。

## 功能特性

- 在一个可编辑的 HTML 文件中提供 16 种经过审查的页面布局
- 采用深色 ZXcharT 主题、金色强调色和响应式布局
- 支持键盘、触控和按钮导航
- 支持卡片点击聚焦和条形图动画，并兼容 `prefers-reduced-motion`
- 提供 POSIX Shell 和仅依赖 Python 3 标准库的项目生成器
- 提供通用 Agent 工作流示例和平台适配指南

## 页面布局

`layout-cover`、`layout-agenda`、`layout-metrics`、`layout-dashboard`、`layout-split`、`layout-bars`、`layout-quote`、`layout-timeline`、`layout-detail`、`layout-stack`、`layout-compare`、`layout-timeline-3col`、`layout-hook`、`layout-statement`、`layout-outro` 和 `layout-closing`。

各布局的适用场景与约束参见 [docs/layouts.md](docs/layouts.md)。

## 快速开始

### macOS / Linux

```sh
sh scripts/new-project.sh "my-deck"
# 然后使用现代浏览器打开 projects/my-deck/index.html。
```

### Windows

```powershell
py scripts/new-project.py "my-deck"
# 然后使用现代浏览器打开 projects\my-deck\index.html。
```

在 macOS/Linux 上使用 Shell 脚本时不需要安装 Python。两个生成器都会根据自身路径定位仓库，并默认在 `projects/` 下创建项目。

## 与 AI Agent 配合使用

向 Agent 提供仓库根目录（或用户指定的输出目录）、任务简报、参考材料和所需的幻灯片顺序，并要求它：

1. 对齐受众、目标与约束；
2. 使用 16 种布局规划内容；
3. 在适当时机请求确认大纲；
4. 复制 `template.html` 生成演示文稿；
5. 预览并核验事实、链接和可读性；
6. 迭代内容并记录尚未解决的问题。

可移植工作流程参见 [AGENTS.md](AGENTS.md) 和 [SKILL.md](SKILL.md)。通用 Agent 示例刻意将执行角色与独立验证角色分开。

## 在线演示 / GitHub Pages

`index.html` 是一个轻量级布局画廊入口，其中嵌入了中性的模板页面。仓库在 `.github/workflows/pages.yml` 中提供仅允许手动触发的 Pages 工作流。只有仓库所有者主动选择 **Run workflow** 时才会运行；克隆或推送仓库都不会自动部署。

项目预期访问地址为 <https://zxchart.github.io/onechartlab-slides/>。本仓库不占用 `onechart.top` 或 `onechartlab.com`。

## 主题定制

在复制出的演示文稿中修改 `:root` 下的 CSS 自定义属性。请继续使用变量表达语义颜色、保持足够的对比度，并在减少动态效果的系统设置下进行测试。[docs/customization.md](docs/customization.md) 介绍了主题变量和字体行为。

## 目标浏览器

本设计面向当前版本的 Chrome、Edge、Firefox 和 Safari，但 v0.1.0 尚未完成正式的四浏览器兼容性矩阵测试。JavaScript 用于导航和可选交互；即使禁用 JavaScript，幻灯片结构仍可查看。Google Fonts 仅作为网络资源引用，无法访问时会回退到系统字体。

## 目录结构

```text
.
├── template.html                 中性模板与布局的唯一事实来源
├── index.html                    布局画廊入口
├── themes/zxchart/design.md      设计变量与布局清单
├── docs/                         布局、定制和平台说明
├── examples/agent-workflow/      通用 Agent 工作流示例
├── scripts/                      可移植生成器与仓库检查器
├── projects/.gitkeep             本地生成项目的占位目录
└── assets/.gitkeep               有意保持为空的预览素材目录
```

## 致谢

模板基础来自 Zara Zhang 的 [beautiful-html-templates](https://github.com/zarazhangrui/beautiful-html-templates)，采用 MIT 许可证。[frontend-slides](https://github.com/zarazhangrui/frontend-slides) 和 [html-presentation](https://github.com/juanjuanjie/html-presentation) 为工作流与演示方法提供了参考。详情参见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) 和 [SOURCES.md](SOURCES.md)。

## 许可证与商标

代码、文档和通用示例采用 [MIT 许可证](LICENSE)。OneChartLab、OneChartLab Slides、ZXcharT 名称及其 Logo 的相关权利保留，详见 [TRADEMARKS.md](TRADEMARKS.md)。
