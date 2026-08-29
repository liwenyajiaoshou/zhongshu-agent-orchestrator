# 中枢 Runtime Deployment Pack

中枢是一个用于长期统筹 ChatGPT + Codex / AI Agent 开发工作的项目级 Runtime。

## 1. 适用条件

**你需要什么：**
- 一个 ChatGPT Project
- 一个正在开发的软件项目（如果需要调用 Codex/Antigravity）

**你不需要：**
- Git
- Python
- GitHub CLI
- Clone 本仓库
- 先安装卫兵

**关于卫兵（可选增强）：**
最低可用只需 ChatGPT Project + 中枢。若需要本地 Agent 执行代码修改，再接入 Codex / Antigravity。如果需要更严格的施工现场治理和防灾保护，再配合卫兵。新手完全可以先只体验网页版中枢统筹。

---

## 2. 新手 5 分钟 Quick Start

要将中枢部署到一个新的 ChatGPT Project 中，只需以下 8 步：

1. 从 Release 页面下载 Latest Runtime Pack (ZIP文件)
2. 解压 ZIP 文件
3. 打开解压后的 `project-upload/` 目录
4. 全选并上传 `project-upload/` 中的所有文件到 ChatGPT Project 的 Project Sources
5. 打开解压根目录的 `PROJECT_INSTRUCTIONS.txt`
6. 复制全文到 ChatGPT Project 的 Project Instructions
7. 发送安装自检提示词（见下）
8. 收到 `ZHONGSHU_RUNTIME_READY` 即部署完成

### 安装自检提示词

开启新对话，发送：

```text
检查中枢是否部署完整。

请只检查当前 Project 已提供的中枢 Runtime：

1. 告诉我检测到的 Runtime 版本；
2. 检查需要的 Project Source 文件是否完整；
3. 检查 Project Instructions 是否已生效；
4. 如果缺少文件，直接告诉我缺哪个；
5. 如果完整，只回复：

ZHONGSHU_RUNTIME_READY

并告诉我下一步如何启动一个新项目。
```

---

## 3. 日常最常用的三句话

部署完成后，这是你最常和中枢说的话：

- **Codex 做完以后：** `按中枢审计这份施工报告。`
- **要下一轮施工：** `生成下一步最小施工方案。`
- **当前线程太长：** `按中枢判断是否应该换线程；如果应该，生成最小充分交接。`

---

## 4. 完整说明与高级用法

完整部署说明、高级用法、升级方式、中枢与卫兵的详细关系、线程策略、故障排查、各版本新特性等，请参阅：

[README_部署与使用.md](README_部署与使用.md)
