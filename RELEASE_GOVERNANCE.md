# Zhongshu Release Governance

本文件规定了中枢（Zhongshu）项目的通用发布规则与硬门标准。

## 1. Tag 与 Release 分离

每个版本必须明确存在两个不同阶段：
- **Stage A — Git Tag**：Git 对 commit 的版本引用
- **Stage B — GitHub Release**：GitHub 基于 Tag 创建的正式发布对象

“Tag 已 push”不再等同于“Release 已发布”。

## 2. Release 创建与验证硬门

未来每个版本发布流程必须显式执行以下步骤：
1. Create annotated tag
2. Push tag
3. Create GitHub Release
4. Verify GitHub Release object

缺少任一步骤，发布状态不得为 PASS。

每个版本发布后，必须使用 `gh release view <TARGET_VERSION>`（或等价 API）进行验证，确保：
- tagName = TARGET_VERSION
- isDraft = false
- isPrerelease = false
- publishedAt != null

并在 `gh release list --limit 20` 中确认目标版本真实出现。

## 3. 禁止弱证据验证

以下证据**不能**单独作为 Release PASS 的凭据：
- Tag 存在
- `git tag --list` 能看到版本
- `git ls-remote` 能看到 refs/tags
- `/releases/tag/<version>` URL 能打开
- 网页出现 tag 名

这只能证明 Tag 层存在，不能证明 Release 对象存在。

## 4. 最新版本验证 (Latest)

每次顺序发布完成后，必须检查当前最高正式版本是否为 **Latest**。如遇异常（且非 prerelease/draft 设置所致），只允许调整 Release 的 Latest 标记，不允许修改 Tag 或重写历史。

## 5. 发布状态标准化

- **PASS**：commit + tag + push + Release object + post-release verification 全部完成。
- **PARTIAL_PUBLISH**：部分完成（例如 Tag 已 push，但 Release 对象未创建）。此时只允许补齐 Release，不回滚 Tag，不 force push。
- **STOPPED**：发现异常需要人工介入，例如远端未知漂移、权限问题、Tag 冲突等。
- **FAIL_CLOSED**：出现致命问题，例如版本源无法验证、发现 Secret 泄漏、需要历史重写等。

## 6. 其他规定

- 禁止历史重写（包括修改旧 Tag 或 amend release commits）。
- 每次任务只发布一个目标版本，禁止顺带批量发布后续版本。
