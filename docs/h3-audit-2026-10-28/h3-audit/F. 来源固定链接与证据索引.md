# F｜来源、版本固定链接与证据边界

审计日：2026-10-28（北京时间）。基线 `093f3129a3f7bd27c74928b1cd31a54fbdebe057`；main 固定为 `d21241f0a4b3acbb34c97dae47fa417b7065e438`。

- [基线提交](https://github.com/MiniMax-AI/MiniMax-H3/commit/093f3129a3f7bd27c74928b1cd31a54fbdebe057)
- [当前提交](https://github.com/MiniMax-AI/MiniMax-H3/commit/d21241f0a4b3acbb34c97dae47fa417b7065e438)
- [完整比较](https://github.com/MiniMax-AI/MiniMax-H3/compare/093f3129a3f7bd27c74928b1cd31a54fbdebe057...d21241f0a4b3acbb34c97dae47fa417b7065e438)

`全文件覆盖清单.csv` 给出全部 229 个文件的 SHA256 和 main 固定链接；基线存在的同路径文件也给出固定链接。MV 迁移前路径另见 B。

## 使用的证据类型

- 【官方仓库事实】仓库已有代码、配置、Skill 流程文字；其中 meta 的 community/official-featured 代表来源分类，不等同于模型质量保证。
- 【维护者说明】标明账号及回复链接；关闭 issue 或合并文档只证明仓库状态，不证明模型质量。
- 【社区报告】issue、PR 作者或回复者自述；本审计未重跑其生成实验。
- 【静态审计发现/推断】由文件冲突、数据流、代码 API 用法推导；明确区分已观察静态事实与未验证运行后果。
- 【未验证】没有模型推理、付费 API 调用、权重加载或视频质量复现实验。ffprobe 只检查现有媒体元数据。

## 仓库逐文件固定来源

- [.agents/skills/h3-prompt-writing/SKILL.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/.agents/skills/h3-prompt-writing/SKILL.md)
- [.agents/skills/h3-prompt-writing/agents/openai.yaml](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/.agents/skills/h3-prompt-writing/agents/openai.yaml)
- [.agents/skills/h3-prompt-writing/references/base-en.txt](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/.agents/skills/h3-prompt-writing/references/base-en.txt)
- [.agents/skills/h3-prompt-writing/references/ref-en.txt](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/.agents/skills/h3-prompt-writing/references/ref-en.txt)
- [.claude/skills/h3-prompt-writing/SKILL.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/.claude/skills/h3-prompt-writing/SKILL.md)
- [.claude/skills/h3-prompt-writing/agents/openai.yaml](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/.claude/skills/h3-prompt-writing/agents/openai.yaml)
- [.claude/skills/h3-prompt-writing/references/base-en.txt](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/.claude/skills/h3-prompt-writing/references/base-en.txt)
- [.claude/skills/h3-prompt-writing/references/ref-en.txt](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/.claude/skills/h3-prompt-writing/references/ref-en.txt)
- [.gitignore](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/.gitignore)
- [FL2VA/audio_vae/config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/audio_vae/config.json)
- [FL2VA/audio_vae/config.yaml](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/audio_vae/config.yaml)
- [FL2VA/audio_vae/dac_activations.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/audio_vae/dac_activations.py)
- [FL2VA/audio_vae/dac_alias_free_act.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/audio_vae/dac_alias_free_act.py)
- [FL2VA/audio_vae/dac_alias_free_filter.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/audio_vae/dac_alias_free_filter.py)
- [FL2VA/audio_vae/dac_alias_free_resample.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/audio_vae/dac_alias_free_resample.py)
- [FL2VA/audio_vae/dac_attn_proj.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/audio_vae/dac_attn_proj.py)
- [FL2VA/audio_vae/dac_audio_vae.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/audio_vae/dac_audio_vae.py)
- [FL2VA/audio_vae/dac_bigvgan.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/audio_vae/dac_bigvgan.py)
- [FL2VA/audio_vae/dac_utils.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/audio_vae/dac_utils.py)
- [FL2VA/audio_vae/metadata.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/audio_vae/metadata.json)
- [FL2VA/audio_vae/minimax_h3_audio_vae.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/audio_vae/minimax_h3_audio_vae.py)
- [FL2VA/model_index.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/model_index.json)
- [FL2VA/processor/chat_template.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/processor/chat_template.json)
- [FL2VA/processor/merges.txt](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/processor/merges.txt)
- [FL2VA/processor/preprocessor_config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/processor/preprocessor_config.json)
- [FL2VA/processor/tokenizer.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/processor/tokenizer.json)
- [FL2VA/processor/tokenizer_config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/processor/tokenizer_config.json)
- [FL2VA/processor/video_preprocessor_config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/processor/video_preprocessor_config.json)
- [FL2VA/processor/vocab.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/processor/vocab.json)
- [FL2VA/text_encoder/chat_template.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/text_encoder/chat_template.json)
- [FL2VA/text_encoder/config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/text_encoder/config.json)
- [FL2VA/text_encoder/merges.txt](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/text_encoder/merges.txt)
- [FL2VA/text_encoder/model.safetensors.index.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/text_encoder/model.safetensors.index.json)
- [FL2VA/text_encoder/preprocessor_config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/text_encoder/preprocessor_config.json)
- [FL2VA/text_encoder/tokenizer.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/text_encoder/tokenizer.json)
- [FL2VA/text_encoder/tokenizer_config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/text_encoder/tokenizer_config.json)
- [FL2VA/text_encoder/video_preprocessor_config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/text_encoder/video_preprocessor_config.json)
- [FL2VA/text_encoder/vocab.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/text_encoder/vocab.json)
- [FL2VA/tokenizer/merges.txt](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/tokenizer/merges.txt)
- [FL2VA/tokenizer/tokenizer.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/tokenizer/tokenizer.json)
- [FL2VA/tokenizer/tokenizer_config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/tokenizer/tokenizer_config.json)
- [FL2VA/tokenizer/vocab.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/tokenizer/vocab.json)
- [FL2VA/transformer/config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/transformer/config.json)
- [FL2VA/transformer/model.safetensors.index.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/transformer/model.safetensors.index.json)
- [FL2VA/video_vae/attention.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/video_vae/attention.py)
- [FL2VA/video_vae/base_module.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/video_vae/base_module.py)
- [FL2VA/video_vae/config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/video_vae/config.json)
- [FL2VA/video_vae/conv.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/video_vae/conv.py)
- [FL2VA/video_vae/flash.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/video_vae/flash.py)
- [FL2VA/video_vae/func.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/video_vae/func.py)
- [FL2VA/video_vae/klvae.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/video_vae/klvae.py)
- [FL2VA/video_vae/minimax_h3_video_vae.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/video_vae/minimax_h3_video_vae.py)
- [FL2VA/video_vae/norm.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/video_vae/norm.py)
- [FL2VA/video_vae/normalize.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/video_vae/normalize.py)
- [FL2VA/video_vae/parallel.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/video_vae/parallel.py)
- [FL2VA/video_vae/source/config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/video_vae/source/config.json)
- [FL2VA/video_vae/utils.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/video_vae/utils.py)
- [FL2VA/video_vae/vae_cnn.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/video_vae/vae_cnn.py)
- [FL2VA/video_vae/vae_module.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/video_vae/vae_module.py)
- [FL2VA/video_vae/vae_processor.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/video_vae/vae_processor.py)
- [FL2VA/video_vae/vae_vit.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/FL2VA/video_vae/vae_vit.py)
- [README.ja.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/README.ja.md)
- [README.ko.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/README.ko.md)
- [README.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/README.md)
- [README.zh-CN.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/README.zh-CN.md)
- [Ref2VA/audio_vae/config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/audio_vae/config.json)
- [Ref2VA/audio_vae/config.yaml](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/audio_vae/config.yaml)
- [Ref2VA/audio_vae/dac_activations.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/audio_vae/dac_activations.py)
- [Ref2VA/audio_vae/dac_alias_free_act.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/audio_vae/dac_alias_free_act.py)
- [Ref2VA/audio_vae/dac_alias_free_filter.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/audio_vae/dac_alias_free_filter.py)
- [Ref2VA/audio_vae/dac_alias_free_resample.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/audio_vae/dac_alias_free_resample.py)
- [Ref2VA/audio_vae/dac_attn_proj.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/audio_vae/dac_attn_proj.py)
- [Ref2VA/audio_vae/dac_audio_vae.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/audio_vae/dac_audio_vae.py)
- [Ref2VA/audio_vae/dac_bigvgan.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/audio_vae/dac_bigvgan.py)
- [Ref2VA/audio_vae/dac_utils.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/audio_vae/dac_utils.py)
- [Ref2VA/audio_vae/metadata.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/audio_vae/metadata.json)
- [Ref2VA/audio_vae/minimax_h3_audio_vae.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/audio_vae/minimax_h3_audio_vae.py)
- [Ref2VA/model_index.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/model_index.json)
- [Ref2VA/processor/chat_template.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/processor/chat_template.json)
- [Ref2VA/processor/merges.txt](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/processor/merges.txt)
- [Ref2VA/processor/preprocessor_config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/processor/preprocessor_config.json)
- [Ref2VA/processor/tokenizer.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/processor/tokenizer.json)
- [Ref2VA/processor/tokenizer_config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/processor/tokenizer_config.json)
- [Ref2VA/processor/video_preprocessor_config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/processor/video_preprocessor_config.json)
- [Ref2VA/processor/vocab.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/processor/vocab.json)
- [Ref2VA/text_encoder/chat_template.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/text_encoder/chat_template.json)
- [Ref2VA/text_encoder/config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/text_encoder/config.json)
- [Ref2VA/text_encoder/merges.txt](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/text_encoder/merges.txt)
- [Ref2VA/text_encoder/model.safetensors.index.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/text_encoder/model.safetensors.index.json)
- [Ref2VA/text_encoder/preprocessor_config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/text_encoder/preprocessor_config.json)
- [Ref2VA/text_encoder/tokenizer.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/text_encoder/tokenizer.json)
- [Ref2VA/text_encoder/tokenizer_config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/text_encoder/tokenizer_config.json)
- [Ref2VA/text_encoder/video_preprocessor_config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/text_encoder/video_preprocessor_config.json)
- [Ref2VA/text_encoder/vocab.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/text_encoder/vocab.json)
- [Ref2VA/tokenizer/merges.txt](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/tokenizer/merges.txt)
- [Ref2VA/tokenizer/tokenizer.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/tokenizer/tokenizer.json)
- [Ref2VA/tokenizer/tokenizer_config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/tokenizer/tokenizer_config.json)
- [Ref2VA/tokenizer/vocab.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/tokenizer/vocab.json)
- [Ref2VA/transformer/config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/transformer/config.json)
- [Ref2VA/transformer/model.safetensors.index.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/transformer/model.safetensors.index.json)
- [Ref2VA/video_vae/attention.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/video_vae/attention.py)
- [Ref2VA/video_vae/base_module.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/video_vae/base_module.py)
- [Ref2VA/video_vae/config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/video_vae/config.json)
- [Ref2VA/video_vae/conv.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/video_vae/conv.py)
- [Ref2VA/video_vae/flash.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/video_vae/flash.py)
- [Ref2VA/video_vae/func.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/video_vae/func.py)
- [Ref2VA/video_vae/klvae.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/video_vae/klvae.py)
- [Ref2VA/video_vae/minimax_h3_video_vae.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/video_vae/minimax_h3_video_vae.py)
- [Ref2VA/video_vae/norm.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/video_vae/norm.py)
- [Ref2VA/video_vae/normalize.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/video_vae/normalize.py)
- [Ref2VA/video_vae/parallel.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/video_vae/parallel.py)
- [Ref2VA/video_vae/source/config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/video_vae/source/config.json)
- [Ref2VA/video_vae/utils.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/video_vae/utils.py)
- [Ref2VA/video_vae/vae_cnn.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/video_vae/vae_cnn.py)
- [Ref2VA/video_vae/vae_module.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/video_vae/vae_module.py)
- [Ref2VA/video_vae/vae_processor.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/video_vae/vae_processor.py)
- [Ref2VA/video_vae/vae_vit.py](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/Ref2VA/video_vae/vae_vit.py)
- [assets/3d-animation-short-generator.gif](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/assets/3d-animation-short-generator.gif)
- [assets/brand-promo-video-generator.gif](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/assets/brand-promo-video-generator.gif)
- [assets/co-op-game-intro-generator.gif](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/assets/co-op-game-intro-generator.gif)
- [assets/fl2va.mp4](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/assets/fl2va.mp4)
- [assets/full-arch.png](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/assets/full-arch.png)
- [assets/h3_direct_2k.mp4](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/assets/h3_direct_2k.mp4)
- [assets/h3_direct_768p.mp4](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/assets/h3_direct_768p.mp4)
- [assets/handdrawn-live-video-generator.gif](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/assets/handdrawn-live-video-generator.gif)
- [assets/i2va.mp4](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/assets/i2va.mp4)
- [assets/i2va_2k.mp4](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/assets/i2va_2k.mp4)
- [assets/i2va_direct_2k.mp4](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/assets/i2va_direct_2k.mp4)
- [assets/i2va_direct_768p.mp4](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/assets/i2va_direct_768p.mp4)
- [assets/minimalist-product-ad-generator.gif](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/assets/minimalist-product-ad-generator.gif)
- [assets/minimax-h3-header.gif](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/assets/minimax-h3-header.gif)
- [assets/music-video-subtitle-generator.gif](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/assets/music-video-subtitle-generator.gif)
- [assets/overview.png](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/assets/overview.png)
- [assets/paper-collage-explainer-generator.gif](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/assets/paper-collage-explainer-generator.gif)
- [assets/papercraft-stop-motion-explainer.gif](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/assets/papercraft-stop-motion-explainer.gif)
- [assets/r2va.mp4](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/assets/r2va.mp4)
- [assets/r2va_2k.mp4](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/assets/r2va_2k.mp4)
- [assets/r2va_direct_2k.mp4](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/assets/r2va_direct_2k.mp4)
- [assets/r2va_direct_768p.mp4](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/assets/r2va_direct_768p.mp4)
- [assets/ref2va.mp4](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/assets/ref2va.mp4)
- [assets/t2va.mp4](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/assets/t2va.mp4)
- [assets/t2va_2k.mp4](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/assets/t2va_2k.mp4)
- [audio_scheduler/scheduler_config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/audio_scheduler/scheduler_config.json)
- [audio_vae/config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/audio_vae/config.json)
- [model_index.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/model_index.json)
- [modular_model_index.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/modular_model_index.json)
- [processor/chat_template.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/processor/chat_template.json)
- [processor/merges.txt](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/processor/merges.txt)
- [processor/preprocessor_config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/processor/preprocessor_config.json)
- [processor/tokenizer.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/processor/tokenizer.json)
- [processor/tokenizer_config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/processor/tokenizer_config.json)
- [processor/video_preprocessor_config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/processor/video_preprocessor_config.json)
- [processor/vocab.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/processor/vocab.json)
- [requirements.txt](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/requirements.txt)
- [scheduler/scheduler_config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/scheduler/scheduler_config.json)
- [scripts/readme/full-2k-i2va-h3-base.sh](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/scripts/readme/full-2k-i2va-h3-base.sh)
- [scripts/readme/full-2k-i2va-h3-context-ir.sh](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/scripts/readme/full-2k-i2va-h3-context-ir.sh)
- [scripts/readme/full-2k-i2va-h3-regenerate-2k.sh](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/scripts/readme/full-2k-i2va-h3-regenerate-2k.sh)
- [scripts/readme/full-2k-i2va-reference-2k-result-by-directly-calling-open-platform-api.sh](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/scripts/readme/full-2k-i2va-reference-2k-result-by-directly-calling-open-platform-api.sh)
- [scripts/readme/full-2k-i2va-reference-768p-result-by-directly-calling-open-platform-api.sh](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/scripts/readme/full-2k-i2va-reference-768p-result-by-directly-calling-open-platform-api.sh)
- [scripts/readme/full-2k-ref2va-h3-api-2k-in-open-platform-for-reference.sh](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/scripts/readme/full-2k-ref2va-h3-api-2k-in-open-platform-for-reference.sh)
- [scripts/readme/full-2k-ref2va-h3-base.sh](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/scripts/readme/full-2k-ref2va-h3-base.sh)
- [scripts/readme/full-2k-ref2va-h3-context-ir.sh](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/scripts/readme/full-2k-ref2va-h3-context-ir.sh)
- [scripts/readme/full-2k-ref2va-reference-2k-result-by-directly-calling-open-platform-api.sh](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/scripts/readme/full-2k-ref2va-reference-2k-result-by-directly-calling-open-platform-api.sh)
- [scripts/readme/full-2k-ref2va-reference-768p-result-by-directly-calling-open-platform-api.sh](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/scripts/readme/full-2k-ref2va-reference-768p-result-by-directly-calling-open-platform-api.sh)
- [scripts/readme/full-2k-t2va-h3-base.sh](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/scripts/readme/full-2k-t2va-h3-base.sh)
- [scripts/readme/full-2k-t2va-h3-context-ir.sh](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/scripts/readme/full-2k-t2va-h3-context-ir.sh)
- [scripts/readme/full-2k-t2va-h3-regenerate-2k.sh](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/scripts/readme/full-2k-t2va-h3-regenerate-2k.sh)
- [scripts/readme/full-2k-t2va-reference-2k-result-by-directly-calling-open-platform-api.sh](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/scripts/readme/full-2k-t2va-reference-2k-result-by-directly-calling-open-platform-api.sh)
- [scripts/readme/full-2k-t2va-reference-768p-result-by-directly-calling-open-platform-api.sh](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/scripts/readme/full-2k-t2va-reference-768p-result-by-directly-calling-open-platform-api.sh)
- [scripts/readme/reproducible-768p-fl2va-request.sh](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/scripts/readme/reproducible-768p-fl2va-request.sh)
- [scripts/readme/reproducible-768p-ref2va-request.sh](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/scripts/readme/reproducible-768p-ref2va-request.sh)
- [scripts/readme/reproducible-768p-t2va-request.sh](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/scripts/readme/reproducible-768p-t2va-request.sh)
- [skills/3d-animation-short-generator/SKILL.cn.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/3d-animation-short-generator/SKILL.cn.md)
- [skills/3d-animation-short-generator/SKILL.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/3d-animation-short-generator/SKILL.md)
- [skills/3d-animation-short-generator/meta.yaml](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/3d-animation-short-generator/meta.yaml)
- [skills/3d-animation-short-generator/references/fallback-policy.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/3d-animation-short-generator/references/fallback-policy.md)
- [skills/3d-animation-short-generator/references/model-selection.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/3d-animation-short-generator/references/model-selection.md)
- [skills/3d-animation-short-generator/references/qc-checklist.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/3d-animation-short-generator/references/qc-checklist.md)
- [skills/3d-animation-short-generator/references/shot-table-spec.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/3d-animation-short-generator/references/shot-table-spec.md)
- [skills/3d-animation-short-generator/references/storyboard-guidelines.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/3d-animation-short-generator/references/storyboard-guidelines.md)
- [skills/README.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/README.md)
- [skills/brand-promo-video-generator/SKILL.cn.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/brand-promo-video-generator/SKILL.cn.md)
- [skills/brand-promo-video-generator/SKILL.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/brand-promo-video-generator/SKILL.md)
- [skills/brand-promo-video-generator/meta.yaml](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/brand-promo-video-generator/meta.yaml)
- [skills/co-op-game-intro-generator/SKILL.cn.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/co-op-game-intro-generator/SKILL.cn.md)
- [skills/co-op-game-intro-generator/SKILL.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/co-op-game-intro-generator/SKILL.md)
- [skills/co-op-game-intro-generator/meta.yaml](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/co-op-game-intro-generator/meta.yaml)
- [skills/co-op-game-intro-generator/references/h3-confirmation-image-template.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/co-op-game-intro-generator/references/h3-confirmation-image-template.md)
- [skills/co-op-game-intro-generator/references/h3-video-prompt-template.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/co-op-game-intro-generator/references/h3-video-prompt-template.md)
- [skills/h3-prompt-writing/SKILL.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/h3-prompt-writing/SKILL.md)
- [skills/h3-prompt-writing/agents/openai.yaml](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/h3-prompt-writing/agents/openai.yaml)
- [skills/h3-prompt-writing/references/base-en.txt](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/h3-prompt-writing/references/base-en.txt)
- [skills/h3-prompt-writing/references/ref-en.txt](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/h3-prompt-writing/references/ref-en.txt)
- [skills/handdrawn-live-video-generator/SKILL.cn.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/handdrawn-live-video-generator/SKILL.cn.md)
- [skills/handdrawn-live-video-generator/SKILL.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/handdrawn-live-video-generator/SKILL.md)
- [skills/handdrawn-live-video-generator/meta.yaml](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/handdrawn-live-video-generator/meta.yaml)
- [skills/minimalist-product-ad-generator/SKILL.cn.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/minimalist-product-ad-generator/SKILL.cn.md)
- [skills/minimalist-product-ad-generator/SKILL.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/minimalist-product-ad-generator/SKILL.md)
- [skills/minimalist-product-ad-generator/meta.yaml](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/minimalist-product-ad-generator/meta.yaml)
- [skills/music-video-subtitle-generator/SKILL.cn.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/music-video-subtitle-generator/SKILL.cn.md)
- [skills/music-video-subtitle-generator/SKILL.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/music-video-subtitle-generator/SKILL.md)
- [skills/music-video-subtitle-generator/meta.yaml](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/music-video-subtitle-generator/meta.yaml)
- [skills/paper-collage-explainer-generator/SKILL.cn.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/paper-collage-explainer-generator/SKILL.cn.md)
- [skills/paper-collage-explainer-generator/SKILL.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/paper-collage-explainer-generator/SKILL.md)
- [skills/paper-collage-explainer-generator/meta.yaml](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/paper-collage-explainer-generator/meta.yaml)
- [skills/papercraft-stop-motion-explainer/SKILL.cn.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/papercraft-stop-motion-explainer/SKILL.cn.md)
- [skills/papercraft-stop-motion-explainer/SKILL.md](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/papercraft-stop-motion-explainer/SKILL.md)
- [skills/papercraft-stop-motion-explainer/meta.yaml](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills/papercraft-stop-motion-explainer/meta.yaml)
- [skills-lock.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/skills-lock.json)
- [text_encoder/chat_template.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/text_encoder/chat_template.json)
- [text_encoder/config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/text_encoder/config.json)
- [text_encoder/merges.txt](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/text_encoder/merges.txt)
- [text_encoder/model.safetensors.index.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/text_encoder/model.safetensors.index.json)
- [text_encoder/preprocessor_config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/text_encoder/preprocessor_config.json)
- [text_encoder/tokenizer.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/text_encoder/tokenizer.json)
- [text_encoder/tokenizer_config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/text_encoder/tokenizer_config.json)
- [text_encoder/video_preprocessor_config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/text_encoder/video_preprocessor_config.json)
- [text_encoder/vocab.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/text_encoder/vocab.json)
- [tokenizer/merges.txt](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/tokenizer/merges.txt)
- [tokenizer/tokenizer.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/tokenizer/tokenizer.json)
- [tokenizer/tokenizer_config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/tokenizer/tokenizer_config.json)
- [tokenizer/vocab.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/tokenizer/vocab.json)
- [transformer/config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/transformer/config.json)
- [transformer/diffusion_pytorch_model.safetensors.index.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/transformer/diffusion_pytorch_model.safetensors.index.json)
- [transformer_ref/config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/transformer_ref/config.json)
- [transformer_ref/diffusion_pytorch_model.safetensors.index.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/transformer_ref/diffusion_pytorch_model.safetensors.index.json)
- [vae/config.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/vae/config.json)
- [vae/diffusion_pytorch_model.safetensors.index.json](https://github.com/MiniMax-AI/MiniMax-H3/blob/d21241f0a4b3acbb34c97dae47fa417b7065e438/vae/diffusion_pytorch_model.safetensors.index.json)

## 基线之后的全部提交

- [e0a5da658eb872757d977ea3781c4b8a20fbe47e](https://github.com/MiniMax-AI/MiniMax-H3/commit/e0a5da658eb872757d977ea3781c4b8a20fbe47e) — 2026-08-06T13:30:48+08:00 — Polish skills README with status and install-name notes
- [319e2008f4a3a520ee11170cb82e43ba3d7f2f69](https://github.com/MiniMax-AI/MiniMax-H3/commit/319e2008f4a3a520ee11170cb82e43ba3d7f2f69) — 2026-08-06T13:32:31+08:00 — Declare skills WIP status and contribution rewards in skills README
- [a71bc89bcc7af80784f0be75a34b9b208fe126c4](https://github.com/MiniMax-AI/MiniMax-H3/commit/a71bc89bcc7af80784f0be75a34b9b208fe126c4) — 2026-08-06T13:33:54+08:00 — Merge pull request #1 from RyanLee-Dev/docs/optimize-skills-readme
- [e57206882b2b0d8df87b03aab91472ba27bcffc3](https://github.com/MiniMax-AI/MiniMax-H3/commit/e57206882b2b0d8df87b03aab91472ba27bcffc3) — 2026-08-06T17:50:51+08:00 — Update README.md
- [edb9ae3bf4023c29e617abf33643ee41aeb46fe0](https://github.com/MiniMax-AI/MiniMax-H3/commit/edb9ae3bf4023c29e617abf33643ee41aeb46fe0) — 2026-08-06T17:51:26+08:00 — Update README.md
- [8d8824efaf94586c0cc9ac7ad8d0723d4d6420ea](https://github.com/MiniMax-AI/MiniMax-H3/commit/8d8824efaf94586c0cc9ac7ad8d0723d4d6420ea) — 2026-08-06T17:52:52+08:00 — Update README.md
- [12ebd6bd8c5d1748a678ac38f4f1238472a98a24](https://github.com/MiniMax-AI/MiniMax-H3/commit/12ebd6bd8c5d1748a678ac38f4f1238472a98a24) — 2026-08-07T16:31:18-03:00 — Add h3-prompt-writing skill installation artifacts
- [1ce88e916de7c15b63cbaf347642503f9bc21d3d](https://github.com/MiniMax-AI/MiniMax-H3/commit/1ce88e916de7c15b63cbaf347642503f9bc21d3d) — 2026-08-07T16:38:02-03:00 — Install h3-prompt-writing skill
- [8e1fa26b0d92ebb1bcdfe84cd9a608482d010f55](https://github.com/MiniMax-AI/MiniMax-H3/commit/8e1fa26b0d92ebb1bcdfe84cd9a608482d010f55) — 2026-08-09T07:14:01+05:30 — Add requirements.txt and fix init_weights for weight_norm Conv1d
- [597042140567efefd8c4adcfe8124c20f63a3399](https://github.com/MiniMax-AI/MiniMax-H3/commit/597042140567efefd8c4adcfe8124c20f63a3399) — 2026-08-09T10:05:36+05:30 — Fix folder/link mismatch for music-video-subtitle-generator skill
- [e4a0b9c23dcbb8870d48a8eecab4bcc4058fc331](https://github.com/MiniMax-AI/MiniMax-H3/commit/e4a0b9c23dcbb8870d48a8eecab4bcc4058fc331) — 2026-08-09T16:33:32+08:00 — Merge pull request #12 from Anuj04432/fix/mv-subtitle-skill-folder-name
- [8317f43ddabe950f3a6c8908090a22c8b0228e4c](https://github.com/MiniMax-AI/MiniMax-H3/commit/8317f43ddabe950f3a6c8908090a22c8b0228e4c) — 2026-08-09T16:33:51+08:00 — Merge pull request #10 from karandhaodiyal28-hash/fix/requirements-txt-and-init-weights
- [b0175e52746879fc92f9243ed0ebcff8393a30b3](https://github.com/MiniMax-AI/MiniMax-H3/commit/b0175e52746879fc92f9243ed0ebcff8393a30b3) — 2026-08-09T16:34:27+08:00 — Merge pull request #8 from isacjosepinha-debug/isacjosepinha-debug-effective-happiness
- [fbe95f7fcb94a74a531750e16ab9288871cebea0](https://github.com/MiniMax-AI/MiniMax-H3/commit/fbe95f7fcb94a74a531750e16ab9288871cebea0) — 2026-08-09T18:05:54+08:00 — Merge pull request #7 from isacjosepinha-debug/isacjosepinha-debug-didactic-winner
- [b7227fa6a6206e9fb30562383d39e53cf3866a48](https://github.com/MiniMax-AI/MiniMax-H3/commit/b7227fa6a6206e9fb30562383d39e53cf3866a48) — 2026-08-09T18:40:41+08:00 — Add multilingual README files
- [b731d8846cf789f284d538013d5caea053c511c8](https://github.com/MiniMax-AI/MiniMax-H3/commit/b731d8846cf789f284d538013d5caea053c511c8) — 2026-08-09T16:27:52+01:00 — docs(skills): clarify h3-prompt-writing is agent-portable, not OpenAI-only
- [c22aafa3073efdc4ad94f8ec82889b9e736331c0](https://github.com/MiniMax-AI/MiniMax-H3/commit/c22aafa3073efdc4ad94f8ec82889b9e736331c0) — 2026-08-09T22:05:04+05:30 — Fix init_weights in dac_utils.py for weight_norm Conv1d layers
- [3f192aa37fe1ac7815ae8026ddff777c2cb98960](https://github.com/MiniMax-AI/MiniMax-H3/commit/3f192aa37fe1ac7815ae8026ddff777c2cb98960) — 2026-08-10T10:37:18+08:00 — Merge pull request #14 from karandhaodiyal28-hash/fix/dac-utils-init-weights-weight-norm
- [05d91ff89f58b665e56424fd66db9ef0351b3015](https://github.com/MiniMax-AI/MiniMax-H3/commit/05d91ff89f58b665e56424fd66db9ef0351b3015) — 2026-08-10T10:41:10+08:00 — Merge pull request #13 from joeVenner/docs/skill-compatibility-notes
- [743d51e83329cbae6c7694f1c7b89576e7c25e07](https://github.com/MiniMax-AI/MiniMax-H3/commit/743d51e83329cbae6c7694f1c7b89576e7c25e07) — 2026-08-10T12:27:54+01:00 — docs(skills): add compatibility fields to Hub-native skills, sync i18n READMEs
- [ca38d0f07369c7c6c4fea207ead8f18043c90e5c](https://github.com/MiniMax-AI/MiniMax-H3/commit/ca38d0f07369c7c6c4fea207ead8f18043c90e5c) — 2026-08-11T02:38:59+05:30 — docs: remove unnecessary backslash escaping in README
- [37866ed9900b212f18a02d60e38fd3cbfc119ab1](https://github.com/MiniMax-AI/MiniMax-H3/commit/37866ed9900b212f18a02d60e38fd3cbfc119ab1) — 2026-08-11T17:25:55+12:00 — docs: fix logical issue in README.md (section_name_hyphen_inconsistent)
- [ed3cda4e66e6174b59bf1b7ac99c2ae2587769fa](https://github.com/MiniMax-AI/MiniMax-H3/commit/ed3cda4e66e6174b59bf1b7ac99c2ae2587769fa) — 2026-08-11T17:06:21+08:00 — Update README.md
- [3d3b0d1356696148f0c3dfc7bce6aa054a45d76a](https://github.com/MiniMax-AI/MiniMax-H3/commit/3d3b0d1356696148f0c3dfc7bce6aa054a45d76a) — 2026-08-11T18:43:59+08:00 — Merge pull request #35 from lunar-me/fix-docs/issue-005
- [fa6891ff7cdaaa03fa4497e89ac64ff169219acf](https://github.com/MiniMax-AI/MiniMax-H3/commit/fa6891ff7cdaaa03fa4497e89ac64ff169219acf) — 2026-08-11T18:44:41+08:00 — Merge pull request #22 from joeVenner/docs/skill-compatibility-notes-part2
- [a107547fa669c509b8e6363fe18378d46ab3066c](https://github.com/MiniMax-AI/MiniMax-H3/commit/a107547fa669c509b8e6363fe18378d46ab3066c) — 2026-08-11T16:55:43+05:30 — docs(h3-prompt-writing): add tips for better results
- [9176a26ae7fcacd69c6cd7a06f660810c7a477fa](https://github.com/MiniMax-AI/MiniMax-H3/commit/9176a26ae7fcacd69c6cd7a06f660810c7a477fa) — 2026-08-11T23:57:34+05:30 — Support local image paths in image loader
- [80365054c7fbaace01ed417076fecd532c1ae0e0](https://github.com/MiniMax-AI/MiniMax-H3/commit/80365054c7fbaace01ed417076fecd532c1ae0e0) — 2026-08-12T17:47:33-07:00 — Merge pull request #27 from yahyadeveloper9/fix-readme-escaping
- [6da473b48daf91e5aebfb56451f8a0b116348df5](https://github.com/MiniMax-AI/MiniMax-H3/commit/6da473b48daf91e5aebfb56451f8a0b116348df5) — 2026-08-13T09:51:29+08:00 — Merge pull request #45 from Umanginigam/fix-local-image-uri
- [d21241f0a4b3acbb34c97dae47fa417b7065e438](https://github.com/MiniMax-AI/MiniMax-H3/commit/d21241f0a4b3acbb34c97dae47fa417b7065e438) — 2026-08-15T16:31:16+08:00 — Merge pull request #44 from GyArmyBrat/improve-skills

## issue / PR 索引及状态快照

公开列表两页发现 50 个 issue、37 个 PR；已额外请求第三页，未发现更多条目。索引反映抓取时可见集合，不保证包含删除、隐藏或私有讨论。API 域名受网络策略限制，使用 GitHub 网页与嵌入 JSON；没有修改网络策略。

issue #18 显示 totalCommentsCount=3，可提取正文的回复仅1条，另两条未取得，不把它们当作已读证据。PR 页的局部 UI 加载错误不影响已保存的可见正文/时间线，但不保证取得所有折叠审查线程。#6 被其他 PR 引用，直接访问404，仅记录引用，不补写其内容。

- [issues #3: 没有requirement.txt ？？](https://github.com/MiniMax-AI/MiniMax-H3/issues/3) — Closed；快照 `sources/issues-3.txt`
- [issues #4: Fail to inference with diffusers](https://github.com/MiniMax-AI/MiniMax-H3/issues/4) — Open；快照 `sources/issues-4.txt`
- [issues #5: H3 is currently the best opensource model](https://github.com/MiniMax-AI/MiniMax-H3/issues/5) — Open；快照 `sources/issues-5.txt`
- [issues #9: qq](https://github.com/MiniMax-AI/MiniMax-H3/issues/9) — Closed；快照 `sources/issues-9.txt`
- [issues #11: Skill folder name doesn't match its documented display name (music-video-subtitle-generator)](https://github.com/MiniMax-AI/MiniMax-H3/issues/11) — Closed；快照 `sources/issues-11.txt`
- [issues #16: Check out my full swift port](https://github.com/MiniMax-AI/MiniMax-H3/issues/16) — Open；快照 `sources/issues-16.txt`
- [issues #17: Ref2VA: multi-subject voice identity can bleed between reference-image subjects](https://github.com/MiniMax-AI/MiniMax-H3/issues/17) — Open；快照 `sources/issues-17.txt`
- [issues #18: Code hangs during inference deployment with vLLM](https://github.com/MiniMax-AI/MiniMax-H3/issues/18) — Open；快照 `sources/issues-18.txt`
- [issues #20: Request for MiniMax-H3 weight download permission](https://github.com/MiniMax-AI/MiniMax-H3/issues/20) — Open；快照 `sources/issues-20.txt`
- [issues #23: 動画](https://github.com/MiniMax-AI/MiniMax-H3/issues/23) — Open；快照 `sources/issues-23.txt`
- [issues #24: 2.11.3 KHTUVwVIVXYZe](https://github.com/MiniMax-AI/MiniMax-H3/issues/24) — Closed as not planned；快照 `sources/issues-24.txt`
- [issues #40: Rreplace the image URL with the path to a locally stored image](https://github.com/MiniMax-AI/MiniMax-H3/issues/40) — Closed；快照 `sources/issues-40.txt`
- [issues #42: MiniMax-H3 inference hangs for a long time with 0% GPU utilization in local SGLang deployment](https://github.com/MiniMax-AI/MiniMax-H3/issues/42) — Open；快照 `sources/issues-42.txt`
- [issues #46: Question: Are MiniMax H3 VAE tile settings configurable?](https://github.com/MiniMax-AI/MiniMax-H3/issues/46) — Open；快照 `sources/issues-46.txt`
- [issues #47: .](https://github.com/MiniMax-AI/MiniMax-H3/issues/47) — Closed as not planned；快照 `sources/issues-47.txt`
- [issues #48: checkpoint inconsistent between original and diffusers](https://github.com/MiniMax-AI/MiniMax-H3/issues/48) — Open；快照 `sources/issues-48.txt`
- [issues #50: 视频开头有少许爆破音](https://github.com/MiniMax-AI/MiniMax-H3/issues/50) — Open；快照 `sources/issues-50.txt`
- [issues #51: 音频开头存在边界幽灵的情况，希望官方关注一下](https://github.com/MiniMax-AI/MiniMax-H3/issues/51) — Closed；快照 `sources/issues-51.txt`
- [issues #56: Apple Silicon MPS: official FL2VA ComfyUI INT8 path fails on aten::_int_mm](https://github.com/MiniMax-AI/MiniMax-H3/issues/56) — Open；快照 `sources/issues-56.txt`
- [issues #57: 【招聘】 MiniMax 视频模型全球开源生态](https://github.com/MiniMax-AI/MiniMax-H3/issues/57) — Open；快照 `sources/issues-57.txt`
- [issues #58: 家里2台4070笔记本 1台3080电脑 怎么可以做个小集群？？？？](https://github.com/MiniMax-AI/MiniMax-H3/issues/58) — Closed；快照 `sources/issues-58.txt`
- [issues #59: Apoloaguilarhernandez@gmail.com
CAPITAL CONTABLE:CC
AUTORIDA APOLO AGUILAR HERNANDEZ - SATM-](https://github.com/MiniMax-AI/MiniMax-H3/issues/59) — CAPITAL CONTABLE:CC；快照 `sources/issues-59.txt`
- [issues #60: 如果是用I2V二採或放大latent都會失敗](https://github.com/MiniMax-AI/MiniMax-H3/issues/60) — Open；快照 `sources/issues-60.txt`
- [issues #61: Prompt length？](https://github.com/MiniMax-AI/MiniMax-H3/issues/61) — Open；快照 `sources/issues-61.txt`
- [issues #62: Use The SageAttention BUG?](https://github.com/MiniMax-AI/MiniMax-H3/issues/62) — Open；快照 `sources/issues-62.txt`
- [issues #63: b](https://github.com/MiniMax-AI/MiniMax-H3/issues/63) — Open；快照 `sources/issues-63.txt`
- [issues #65: Question: Can modality row selection be moved before the output projections?](https://github.com/MiniMax-AI/MiniMax-H3/issues/65) — Open；快照 `sources/issues-65.txt`
- [issues #68: BUG: All spoken lines sung](https://github.com/MiniMax-AI/MiniMax-H3/issues/68) — Open；快照 `sources/issues-68.txt`
- [issues #69: 动作迁移效果不好，音频对不齐，动作好像也不是很一致](https://github.com/MiniMax-AI/MiniMax-H3/issues/69) — Open；快照 `sources/issues-69.txt`
- [issues #70: av.error.ArgumentError: Invalid argument: 'avcodec_send_frame()' returned 22](https://github.com/MiniMax-AI/MiniMax-H3/issues/70) — Open；快照 `sources/issues-70.txt`
- [issues #72: Minimax H3 vs Seedance 2.0, minimax h3 as good as seedance2.0! Unbelievable!!! WOW!](https://github.com/MiniMax-AI/MiniMax-H3/issues/72) — Open；快照 `sources/issues-72.txt`
- [issues #73: minimax h3微调线稿风格的视频生成用于动画制作，有什么建议吗？](https://github.com/MiniMax-AI/MiniMax-H3/issues/73) — Open；快照 `sources/issues-73.txt`
- [issues #74: 高动态太糊了2.0 50步都救不了](https://github.com/MiniMax-AI/MiniMax-H3/issues/74) — Open；快照 `sources/issues-74.txt`
- [issues #75: 考虑开源没蒸馏CFG的权重版本吗](https://github.com/MiniMax-AI/MiniMax-H3/issues/75) — Open；快照 `sources/issues-75.txt`
- [issues #76: Salam](https://github.com/MiniMax-AI/MiniMax-H3/issues/76) — Open；快照 `sources/issues-76.txt`
- [issues #78: a YouTube video about Jordan](https://github.com/MiniMax-AI/MiniMax-H3/issues/78) — Open；快照 `sources/issues-78.txt`
- [issues #79: Adding minimax support to brain](https://github.com/MiniMax-AI/MiniMax-H3/issues/79) — Open；快照 `sources/issues-79.txt`
- [issues #80: R2V fail to translate Mandarin to Cantonese](https://github.com/MiniMax-AI/MiniMax-H3/issues/80) — Open；快照 `sources/issues-80.txt`
- [issues #81: 台词说什么画面就会变出什么，太扯了](https://github.com/MiniMax-AI/MiniMax-H3/issues/81) — Open；快照 `sources/issues-81.txt`
- [issues #82: H3 ignores/refuses weather (snowfall) and breath-vapor instructions; coat-transfer causes persistent garment penetration; object duplication under high-angle framing](https://github.com/MiniMax-AI/MiniMax-H3/issues/82) — Open；快照 `sources/issues-82.txt`
- [issues #84: MiniMax H3 Ref2VA: Significant Reference-Fidelity Regression in Local ComfyUI](https://github.com/MiniMax-AI/MiniMax-H3/issues/84) — Open；快照 `sources/issues-84.txt`
- [issues #85: MiniMax H3 full INT8/BF16 are unstable in ComfyUI; pruned is fine](https://github.com/MiniMax-AI/MiniMax-H3/issues/85) — Open；快照 `sources/issues-85.txt`
- [issues #86: EVERY SINGLE GENERATION PUTS ON WEDDING RING!!! MAKE IT STOP!!!](https://github.com/MiniMax-AI/MiniMax-H3/issues/86) — Open；快照 `sources/issues-86.txt`
- [issues #87: ،her](https://github.com/MiniMax-AI/MiniMax-H3/issues/87) — Open；快照 `sources/issues-87.txt`
- [issues #88: Subject: Architectural Blueprint: Five-Stage Modular AI Video Pipeline with Stage-Isolated VRAM Caching, Environment-Aware Physics, and Spatial Audio Rendering](https://github.com/MiniMax-AI/MiniMax-H3/issues/88) — Open；快照 `sources/issues-88.txt`
- [issues #89: The sparse-attention version release plan](https://github.com/MiniMax-AI/MiniMax-H3/issues/89) — Open；快照 `sources/issues-89.txt`
- [issues #92: loss of init.py](https://github.com/MiniMax-AI/MiniMax-H3/issues/92) — Open；快照 `sources/issues-92.txt`
- [issues #94: حين تصبح المهارة المرفوضة هي سلاح الدمار الشامل](https://github.com/MiniMax-AI/MiniMax-H3/issues/94) — Open；快照 `sources/issues-94.txt`
- [issues #95: MiniMax H3: extra/repeated Mandarin dialogue and clipped speech onset when using standalone reference audio](https://github.com/MiniMax-AI/MiniMax-H3/issues/95) — Open；快照 `sources/issues-95.txt`
- [issues #96: Render-level probe: assistant-marker injection survives chat-template rendering (downstream unverified)](https://github.com/MiniMax-AI/MiniMax-H3/issues/96) — Open；快照 `sources/issues-96.txt`
- [pull #1: Polish skills README with status and contribution notes](https://github.com/MiniMax-AI/MiniMax-H3/pull/1) — Merged；快照 `sources/pull-1.txt`
- [pull #2: docs: encourage skill contributions with API credit rewards](https://github.com/MiniMax-AI/MiniMax-H3/pull/2) — Closed；快照 `sources/pull-2.txt`
- [pull #7: Add h3-prompt-writing skill installation](https://github.com/MiniMax-AI/MiniMax-H3/pull/7) — Merged；快照 `sources/pull-7.txt`
- [pull #8: Install h3-prompt-writing skill](https://github.com/MiniMax-AI/MiniMax-H3/pull/8) — Merged；快照 `sources/pull-8.txt`
- [pull #10: Add requirements.txt and fix init_weights for weight_norm Conv1d](https://github.com/MiniMax-AI/MiniMax-H3/pull/10) — Merged；快照 `sources/pull-10.txt`
- [pull #12: Fix folder/link mismatch for music-video-subtitle-generator skill](https://github.com/MiniMax-AI/MiniMax-H3/pull/12) — Merged；快照 `sources/pull-12.txt`
- [pull #13: docs(skills): clarify h3-prompt-writing is agent-portable, not OpenAI-only](https://github.com/MiniMax-AI/MiniMax-H3/pull/13) — Merged；快照 `sources/pull-13.txt`
- [pull #14: Fix init_weights in dac_utils.py for weight_norm Conv1d layers](https://github.com/MiniMax-AI/MiniMax-H3/pull/14) — Merged；快照 `sources/pull-14.txt`
- [pull #15: Create SECURITY.md for security policy](https://github.com/MiniMax-AI/MiniMax-H3/pull/15) — Closed；快照 `sources/pull-15.txt`
- [pull #19: Fix login bug](https://github.com/MiniMax-AI/MiniMax-H3/pull/19) — Open；快照 `sources/pull-19.txt`
- [pull #22: docs(skills): add compatibility fields to Hub-native skills, sync i18n READMEs](https://github.com/MiniMax-AI/MiniMax-H3/pull/22) — Merged；快照 `sources/pull-22.txt`
- [pull #25: Readme changes](https://github.com/MiniMax-AI/MiniMax-H3/pull/25) — Closed；快照 `sources/pull-25.txt`
- [pull #26: Update full-2k-i2va-h3-base.sh](https://github.com/MiniMax-AI/MiniMax-H3/pull/26) — Closed；快照 `sources/pull-26.txt`
- [pull #27: docs: remove unnecessary backslash escaping in README](https://github.com/MiniMax-AI/MiniMax-H3/pull/27) — Merged；快照 `sources/pull-27.txt`
- [pull #28: Create Marcus WiseLayne](https://github.com/MiniMax-AI/MiniMax-H3/pull/28) — Closed；快照 `sources/pull-28.txt`
- [pull #29: docs: fix logical issue in README.md](https://github.com/MiniMax-AI/MiniMax-H3/pull/29) — Closed；快照 `sources/pull-29.txt`
- [pull #30: docs: fix logical issue in README.md](https://github.com/MiniMax-AI/MiniMax-H3/pull/30) — Closed；快照 `sources/pull-30.txt`
- [pull #31: docs: fix logical issue in skills/minimalist-product-ad-generator/SKILL.md](https://github.com/MiniMax-AI/MiniMax-H3/pull/31) — Closed；快照 `sources/pull-31.txt`
- [pull #32: docs: fix grammar issue in skills/3d-animation-short-generator/SKILL.md](https://github.com/MiniMax-AI/MiniMax-H3/pull/32) — Closed；快照 `sources/pull-32.txt`
- [pull #33: docs: fix grammar issue in skills/co-op-game-intro-generator/SKILL.md](https://github.com/MiniMax-AI/MiniMax-H3/pull/33) — Closed；快照 `sources/pull-33.txt`
- [pull #34: docs: fix grammar issue in README.md](https://github.com/MiniMax-AI/MiniMax-H3/pull/34) — Closed；快照 `sources/pull-34.txt`
- [pull #35: docs: fix logical issue in README.md](https://github.com/MiniMax-AI/MiniMax-H3/pull/35) — Merged；快照 `sources/pull-35.txt`
- [pull #36: docs: fix grammar issue in h3-video-prompt-template.md](https://github.com/MiniMax-AI/MiniMax-H3/pull/36) — Closed；快照 `sources/pull-36.txt`
- [pull #37: Fix MiniMax-H3 dependency versions and Diffusers links](https://github.com/MiniMax-AI/MiniMax-H3/pull/37) — Open；快照 `sources/pull-37.txt`
- [pull #38: Poll asynchronous jobs before downloading example outputs](https://github.com/MiniMax-AI/MiniMax-H3/pull/38) — Open；快照 `sources/pull-38.txt`
- [pull #39: Create SECURITY.MD for security policy and reporting](https://github.com/MiniMax-AI/MiniMax-H3/pull/39) — Closed；快照 `sources/pull-39.txt`
- [pull #43: Add initial devcontainer configuration](https://github.com/MiniMax-AI/MiniMax-H3/pull/43) — Closed；快照 `sources/pull-43.txt`
- [pull #44: docs(h3-prompt-writing): add tips for better results](https://github.com/MiniMax-AI/MiniMax-H3/pull/44) — Merged；快照 `sources/pull-44.txt`
- [pull #45: docs: clarify local image support in conditions.uri](https://github.com/MiniMax-AI/MiniMax-H3/pull/45) — Merged；快照 `sources/pull-45.txt`
- [pull #49: Merge pull request #1 from MiniMax-AI/mainname: Python application

on: [push, pull_request]

jobs: 
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Install deps
        run: |
          python -m pip install --upgrade pip
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
          pip install flake8 pytest || true
      - name: Lint
        run: |
          flake8. --count --select=E9,F63,F7,F82 --show-source --statistics || true
      - name: Test
        run: |
          pytest -q || echo "no tests - ok"](https://github.com/MiniMax-AI/MiniMax-H3/pull/49) — on: [push, pull_request]；快照 `sources/pull-49.txt`
- [pull #66: docs: fix stray escaped pipe in README output resolution row](https://github.com/MiniMax-AI/MiniMax-H3/pull/66) — Open；快照 `sources/pull-66.txt`
- [pull #67: Add skill: h3-character-eval — calibrated character-retention measurement](https://github.com/MiniMax-AI/MiniMax-H3/pull/67) — Open；快照 `sources/pull-67.txt`
- [pull #71: feat(video-vae): expose temporal chunk callback](https://github.com/MiniMax-AI/MiniMax-H3/pull/71) — Closed；快照 `sources/pull-71.txt`
- [pull #77: docs: note 32GB Mac memory limitation](https://github.com/MiniMax-AI/MiniMax-H3/pull/77) — Closed；快照 `sources/pull-77.txt`
- [pull #83: Add files via upload](https://github.com/MiniMax-AI/MiniMax-H3/pull/83) — Open；快照 `sources/pull-83.txt`
- [pull #90: DRAFT - Level Of Token - 2.6x dit speed up](https://github.com/MiniMax-AI/MiniMax-H3/pull/90) — Closed；快照 `sources/pull-90.txt`
- [pull #91: DRAFT - Level Of Token - 2.6x DiT speed up (LoT only)](https://github.com/MiniMax-AI/MiniMax-H3/pull/91) — Draft；快照 `sources/pull-91.txt`

## 延伸核查的外部来源

- [PyTorch v2.4.0 parametrizations.weight_norm](https://github.com/pytorch/pytorch/blob/v2.4.0/torch/nn/utils/parametrizations.py) — 实际参数为 parametrizations.weight.original0/original1；本地保存文本。tag 链接单独标记，下面另附其解析出的提交固定链接（若解析成功）。
- [ComfyUI #16589](https://github.com/Comfy-Org/ComfyUI/issues/16589) — Ref2VA保真回归讨论；Open。
- [ComfyUI PR #15902](https://github.com/Comfy-Org/ComfyUI/pull/15902) — MPS padding 替代方案；抓取时 Open。
- [该PR提交 613e7b0](https://github.com/Comfy-Org/ComfyUI/commit/613e7b068a084cc687c0a6d37daf4739fd69dcbe) — 未据此宣称已发布。
- [PyTorch #194922](https://github.com/pytorch/pytorch/issues/194922) — MPS temporal padding；抓取时 Closed，具体合并/发版边界见报告。
- [higgsfield CLI #94](https://github.com/higgsfield-ai/cli/issues/94) — 多行 prompt 截断报告；Open。

外部 API、HF 权重许可、SGLang cookbook 等是仓库引用的部署依赖，本次未对其所有当前页面/API contract 做端到端验证。license 的准确适用条件应以模型许可原文为准，不照抄 issue #20 路人意见作为法律结论。

## 离线材料与只读记录

`sources/main/skills` 和 `sources/baseline/skills` 保留完整技能树（含全部 references、模板、示例、metadata）；main 的两套隐藏安装副本也保留。`baseline-main.diff` 是完整 patch；`issues-structured.json` 含 issue 作者、回复账号、时间和链接；其余 txt 是公开页面的文本快照，已移除发现的临时签名/通知 URL 参数。HTML 原始抓取文件不纳入最终分享包。

没有执行仓库 shell 请求脚本；只做 bash -n、Python AST 和 JSON解析。没有安装、更新或替换用户现有 H3、ComfyUI、Python依赖、权重或工作流。现有 /workspace/prompt 未改动。V01–V12原方案未在工作区找到，E的编号是临时映射而非原稿逐字diff。

## 外部固定提交补充与状态细化

- [PyTorch weight_norm 不可变源码](https://github.com/pytorch/pytorch/blob/d990dada86a8ad94882b5c23e859b88c0c255bda/torch/nn/utils/parametrizations.py)：v2.4.0 的 tag 解析提交；与读取的官方raw源码一致。
- [PyTorch PR195147](https://github.com/pytorch/pytorch/pull/195147)：页面Closed，但bot有Merged标签和落地提交；不能只按紫色/灰色状态判断。
- [PyTorch修复落地commit](https://github.com/pytorch/pytorch/commit/72bca5e6d542341e6bcd795aaa293968843c29b2)：与issue194922关闭关联；轮子发版覆盖未实测。
- [H3 #51维护者原回复](https://github.com/MiniMax-AI/MiniMax-H3/issues/51#issuecomment-5364674789)：RyanLee-Dev，2026-08-21，答复下个版本修复。

无关/证据不足条目仍留在issue-PR来源索引中供追查：招聘、推广、无描述、无关上传不作为模型故障；#16 Swift port、#88五阶段架构、#79集成诉求属于社区生态/提案，不是当前main能力；#75未蒸馏CFG请求不等于已发布权重。PR71 callback已关闭未入main；PR77“32GB Mac不支持”文档提议已关闭未合并，也不能覆盖#56后来不同第三方路径的成功自述。
