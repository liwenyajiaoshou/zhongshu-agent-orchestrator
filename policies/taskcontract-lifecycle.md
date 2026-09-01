# TaskContract 生命周期决策规则

## 定位

中枢只判断“当前 contract 是否继续、是否需要被新 contract 取代、是否应停止并重新规划”。

中枢不实现 TaskContract 本体、TestPlan、required tests 或 Closure engine。

## 决策值

```text
CONTINUE_CURRENT_CONTRACT
SUPERSEDE_CONTRACT
STOP_AND_REPLAN
```

### CONTINUE_CURRENT_CONTRACT

满足多数条件时继续：

- 主目标未改变；
- 风险边界未改变；
- blocker 仍属当前任务主链路；
- 可通过当前 scope 内局部修复闭环。

### SUPERSEDE_CONTRACT

仅在明确任务边界变化时：

- 当前 contract 已 Closure；
- 正式阶段目标变化；
- 主任务发生实质变化；
- 新阶段需要新的 authoritative contract。

### STOP_AND_REPLAN

出现以下情况停止并重新规划：

- 风险实质升级；
- 产品方向变化；
- 外部事实推翻原设计；
- 需要 Owner 决策；
- 将发生生产、正式数据、跨仓库等高风险变化；
- 当前 contract 已无法诚实表达真实任务目标或边界。

## blocker 不是 supersession 的充分条件

```text
出现 blocker
≠
自动新建 TaskContract
```

若 blocker 仍属于当前主链路，默认 `CONTINUE_CURRENT_CONTRACT`。

## 非目标

不维护第二套 TaskContract 状态机；不跨项目修改卫兵内部实现。
