# 课程内容处理工作流

一个自动化的课程内容处理工作流，帮助您从视频课程中提取、整理和组织知识点。

## 功能特点

- 🎥 视频字幕提取
- 📝 AI 驱动的内容总结
- 🗺️ 自动生成思维导图
- 📚 Markdown 笔记生成
- 🔍 重点内容提取
- 📊 知识点可视化

## 工作流程

1. **内容获取**
   - 视频字幕提取（SubtitleEdit）
   - 语音识别转写（Whisper）
   - 文本预处理

2. **内容处理**
   - DeepSeek AI 分析
   - 重点提取
   - 知识点整理
   - 结构化转换

3. **内容输出**
   - Markdown 文档
   - 思维导图
   - 知识卡片
   - 复习提纲

## 使用方法

### 1. 环境准备

- 安装 SubtitleEdit
- 配置 DeepSeek API
- 安装必要的依赖

### 2. 处理流程

1. 运行字幕提取：
   ```bash
   python extract_subtitle.py --video path/to/video
   ```

2. 生成内容总结：
   ```bash
   python generate_summary.py --input subtitle.txt
   ```

3. 创建思维导图：
   ```bash
   python create_mindmap.py --input summary.md
   ```

### 3. 自定义配置

编辑 `config.yaml` 文件来自定义：
- 输出格式
- AI 模型参数
- 模板样式
- 导出选项

## 目录结构

```
course-content-processor/
├── scripts/
│   ├── extract_subtitle.py
│   ├── generate_summary.py
│   └── create_mindmap.py
├── templates/
│   ├── markdown_template.md
│   ├── mindmap_template.md
│   └── summary_template.md
├── config/
│   └── config.yaml
└── output/
    ├── subtitles/
    ├── summaries/
    └── mindmaps/
```

## 配置文件示例

```yaml
# config.yaml
output:
  format:
    - markdown
    - mindmap
    - summary
  style:
    markdown:
      headers: ["#", "##", "###"]
      emphasis: ["**", "*", "`"]
    mindmap:
      format: "markdown"
      levels: 3
  templates:
    summary: "templates/summary_template.md"
    mindmap: "templates/mindmap_template.md"
```

## 提示词模板

### 1. 内容总结模板

```markdown
请分析以下课程内容：
1. 提取关键知识点（按重要性排序）
2. 标注教师特别强调的部分
3. 生成简要的复习提纲
4. 添加实践建议

课程内容：
[字幕内容]
```

### 2. 思维导图模板

```markdown
请将内容转换为思维导图格式：
1. 使用 Markdown 列表格式
2. 最多 3 层层级
3. 包含关键概念和示例
4. 突出重点内容

内容：
[总结内容]
```

## 注意事项

1. 确保视频文件质量良好
2. 定期更新 AI 模型和配置
3. 备份重要的输出文件
4. 检查生成内容的准确性

## 贡献指南

欢迎提交 Issue 和 Pull Request 来改进工作流程！

## 许可证

MIT License