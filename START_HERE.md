# 第一步：上传文件

把 `project-upload/` 里的所有文件，全部上传到当前 ChatGPT Project 的 **Project Sources**（项目文件）。

# 第二步：设置启动器

打开本目录下的 `PROJECT_INSTRUCTIONS.txt`，复制全文，然后粘贴到 ChatGPT Project 的 **Project Instructions**（项目指令）中并保存。

# 第三步：安装自检

复制以下提示词，发送给 ChatGPT 开启一个新对话：

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

# 成功标志

当你看到 `ZHONGSHU_RUNTIME_READY` 时，部署即告完成。

# 需要高级说明？

如果你需要了解更高级的用法、线程治理策略或如何与卫兵配合，请参阅：
[README_部署与使用.md](https://github.com/liwenyajiaoshou/zhongshu-agent-orchestrator/blob/main/README_%E9%83%A8%E7%BD%B2%E4%B8%8E%E4%BD%BF%E7%94%A8.md) 或官方代码仓库的在线文档。
