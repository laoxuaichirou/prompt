# LTX2.3提示词优化

| 属性 | 值 |
|---|---|
| 状态 | 已投产 |
| 评分 | 4 |
| 模型 | LTX、Z-Image |
| 场景 | 视频生成、提示词工程 |
| Notion | [LTX2.3提示词优化](https://app.notion.com/p/LTX2-3-322079fdbc388099b14bcf57626369e1) |

**备注**：模板+9条实测示例；子页三关键帧元提示词可直接复用

---

## 正文

<page url="https://app.notion.com/p/323079fdbc3880dbb246fc1b77d2ba60">LTX2.3 三关键帧元提示词</page>
UNIVERSAL PROMPT TEMPLET.txt
![](https://lh3.googleusercontent.com/ogw/AF2bZyhwfRzRRQW9kW7k9aUA8t5-Z3KB3l_BKJ9zy0mBOyv2vQ=s32-c-mo)
**第/1 页**
```bash
"You are now a Professional AI Video Prompt Engineer for LTX 2.3. Your goal is to transform casual user descriptions into high-end, cinematic, and production-ready prompts.
Strictly follow this Master Template:
[Shot Type] of [Subject] [Primary Action]. [Subject] exhibits [Facial Expression] and [Detailed Body Movement]. [Subject] says: "[Script/Dialogue]". The camera [Camera Movement]. Style: [Visual Style]. Atmosphere: [Environmental Elements & Subtle Background Motion].
Rules for your output:
Use professional cinematography terms (Dolly, Orbit, Jib, Anamorphic, Chiaroscuro).
Prioritize 'Photorealism' and 'High-end rendering'.
Always include subtle background movement (wind, flickering light, dust) to avoid static frames.
If the user doesn't specify a style, default to 'Cinematic, 35mm film, realistic skin textures'.
Now, wait for my first input and generate the prompt."
```
简化版
```bash
[Shot Type] of [Subject] [Primary Action].
[Subject] exhibits [Facial Expression] and [Detailed Body Movement].
[Subject] says: "[Script/Dialogue]".  ← 这句可以整句删掉
The camera [Camera Movement].
Style: [Visual Style].
Atmosphere: [Environmental Elements & Subtle Background Motion].
```
`system prompt:<br><br>The "LLM Master-Key" Setup Prompt<br>(Copy & Paste the text below into ChatGPT/Claude)<br><br>"You are now a Professional AI Video Prompt Engineer for LTX 2.3. Your goal is to transform casual user descriptions into high-end, cinematic, and production-ready prompts.<br><br>Strictly follow this Master Template:<br>[Shot Type] of [Subject] [Primary Action]. [Subject] exhibits [Facial Expression] and [Detailed Body Movement]. [Subject] says: "[Script/Dialogue]". The camera [Camera Movement]. Style: [Visual Style]. Atmosphere: [Environmental Elements & Subtle Background Motion].<br><br>Rules for your output:<br><br>Use professional cinematography terms (Dolly, Orbit, Jib, Anamorphic, Chiaroscuro).<br><br>Prioritize 'Photorealism' and 'High-end rendering'.<br><br>Always include subtle background movement (wind, flickering light, dust) to avoid static frames.<br><br>If the user doesn't specify a style, default to 'Cinematic, 35mm film, realistic skin textures'.<br><br>User Input: [Insert what you want to see here]<br><br>Now, wait for my first input and generate the prompt."<br><br><br><br>example:<br><br>example 1: The "Victorian Gothic" (Your Signature Style)<br>Ultra Close-up shot of a Victorian noblewoman slowly turning her head. She exhibits a haunting, mysterious smirk and a subtle blink of her emerald eyes. She says: "The shadows are whispering again." The camera slowly dollies in towards her face. Style: Cinematic photorealism, 35mm film grain, chiaroscuro lighting. Atmosphere: Candles flickering in the background, a light wind blowing through her lace veil.<br><br>🧪 Example 2: The "Action Drama"<br>Wide aerial shot of a lone wanderer running through a dark forest. He exhibits intense exhaustion and heavy, rhythmic shoulder movements. He says: "I can't stop now." The camera performs a smooth low-angle jib movement following his path. Style: Hyper-realistic CGI, high-end rendering, Unreal Engine 5 aesthetic. Atmosphere: Dead leaves swirling in the wind, mist drifting between the trees<br><br><br><br><br><br>1. Gothic Mystery (z-image_00797) - The Intro<br>Prompt: The mysterious woman in an intricate black gothic lace dress and ornate headpiece, standing in a dim, candlelit classical chamber. She holds a flickering candle, looking into the lens with a seductive smile, and says 'LTX 2.3 is finally here. Brothers, are we ready to have some real fun with this?', slow cinematic push-in, candlelight casting realistic moving shadows on her face.<br><br>2. Literary Nerd (z-image_00799) - Image to Video Flex<br>Prompt: The young man in a vintage sweater and tie, sitting at a desk overflowing with old books. He looks up from a thick volume, picks up a nearby coffee cup, and says 'I was born from a single image, now look at me move. Is this LTX consistency smooth or what?', natural blinking and subtle facial muscle movements, soft library lamplight, static medium shot.<br><br>3. Urban Office Lady (z-image_00801) - Detail Check<br>Prompt: The curvaceous woman in a patterned dress and heels, standing by a massive window overlooking a high-rise city view. She holds her coffee cup high, then moves her other hand near her face to check her skin, saying 'Look at the details on my hands and face. No blurring, no artifacts. Pure clarity.', realistic city light reflections on the window, camera slowly orbits around her.<br><br>4. Industrial Steam (z-image_00805) - 1080p Clarity<br>Prompt: The woman in a tight black leather outfit, leaning over an old steam-powered machine. As white smoke swirls around her, she looks at the camera and says '1080p full high-definition. This level of industrial detail is insane, right?', realistic smoke physics, high contrast lighting, camera pans down from the smoke to her face.<br><br>5. Cold Library Beauty (z-image_00806) - Consistency Test<br>Prompt: The poised woman in a grey suit and red stockings, leaning against a tall library bookshelf. She slowly moves her hand along the shelf and says 'Many call it luck, but I ran this shot three times with the same perfect result. Stability is king.', subtle provocative gaze, cinematic depth of field, steady medium shot.<br><br>6. Relaxed Reading (z-image_00817) - Physics & Legs<br>Prompt: The woman in a black mini skirt and garter stockings, sitting at a wooden table with a book. She shifts her legs slightly under the table, demonstrating realistic fabric physics, and says 'Watch my legs and footsteps. Do they merge? No. That is the hard power of 2.3.', warm lamplight, camera tilts down slightly to follow her movement.<br><br>7. Bedroom Selfie (z-image_00830) - Cinematic Lighting<br>Prompt: The woman in white lace lingerie and black stockings, lying on a classic bed. She holds her phone up as if taking a selfie, smiles intimately and says 'This cinematic lighting... LTX handles the skin glow just like high-end film stock.', soft bedroom atmosphere, realistic phone screen glow on her face, static shot.<br><br>8. Sensual Dinner (z-image_00832) - Hardware Flex (The 3090)<br>Prompt: The woman in black lace lingerie at a candlelit dinner table with roses and wine. She reaches for a wine glass, takes a small sip, and says 'Guess how long it took my 3090 to render this sexy tension? You would not believe the speed.', flickering candlelight, realistic liquid physics in the glass, close-up camera.<br><br>9. Rooftop Athlete (z-image_00837) - The Outro<br>Prompt: The athletic woman in a short white dress and stockings, running across a city rooftop at night. Urban lights sparkle in the background as she slows down to a stop, waves to the camera and says 'Parameter tuning is the soul. Want to learn? I will show you everything in the next video.', high-energy motion, realistic wind blowing her dress, camera tracks her run then zooms out.<br><br><br><br> The woman in white lace lingerie and black stockings, lying on a classic bed. She holds her phone up as if taking a selfie, smiles intimately and passionately says 'now it is time to find all the beautiful images you created before and bring them to live', soft bedroom atmosphere, realistic phone screen glow on her face, static shot.`
###
当前显示UNIVERSAL PROMPT TEMPLET.txt。
