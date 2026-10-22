# VID-SOC-03 章节过渡空镜

原创模板 · social

## 使用输入

`chapter`, `duration_seconds`, `motion`, `palette`, `scene`

## 提示词

```text
为章节 {{chapter}} 生成{{duration_seconds}}秒过渡空镜：{{scene}}，{{motion}}，{{palette}}，16:9，中心留白用于Remotion章节标题，镜头平稳，无字无对白。
```

## 验收

- 参考资产实际传入
- 单镜头动作可完成
- 检查身份与空间连续性
- 时长和音频满足镜头表

提示词不是API参数；先核对供应商输入类型、时长、画幅、音频与参考数量，不能凭示例模型名推断支持。
