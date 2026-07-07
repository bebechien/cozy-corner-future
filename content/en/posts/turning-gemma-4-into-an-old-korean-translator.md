+++
title = "Turning Gemma 4 into an Old Korean Translator"
date = "2026-06-15"
cover = "images/tuning-gemma-4-into-an-old-korean-translator.png"
tags = ["Fine-tuning", "Gemma", "AI"]
description = "How I fine-tuned Gemma 4 to translate Classical Korean into Modern Korean."
showFullContent = false
readingTime = false
hideComments = false
+++

There’s something uniquely beautiful about old books. The smell of weathered paper, the texture of the pages, and the stories that have survived generations. But if you’ve ever tried opening a piece of Classical Korean literature—like the Joseon Dynasty novel *[HongGildongJeon (홍길동전)](https://en.wikipedia.org/wiki/Hong_Gildong_jeon)*—you’ll quickly realize that time leaves its own mark on language.

Between the lack of word spacing and obsolete letters like the dot vowel *Arae-a (ㆍ)* or the soft *Yeorin-hieut (ㆆ)*, reading it feels less like browsing a novel and more like solving a beautiful, ancient puzzle. Even for native speakers, the linguistic gap is massive.

So, that's why I decided to creat [this tutorial](https://colab.research.google.com/github/google-gemma/cookbook/blob/main/tutorials/Translator_of_Old_Korean_Literature.ipynb), a digital bridge between the past and the present. Using **[Gemma 4 E2B (IT)](https://huggingface.co/google/gemma-4-E2B-it)**, I set out to create a humble translator that turns Classical Korean into smooth, modern Korean.

# The Recipe for Training

To keep things manageable, I ran this on a single NVIDIA T4 GPU (16GB) using Google Colab.

## 1. Setting Up the Kitchen

First, we pull in our favorite open-source tools: Hugging Face’s `transformers`, `trl` for the training loop, and `peft` so we can use LoRA (Low-Rank Adaptation) to fine-tune our model without needing a massive server cluster.

## 2. Gathering the Ingredients

For our data, I used a public domain version of *[HongGildongJeon](https://ko.wikisource.org/wiki/%ED%99%8D%EA%B8%B8%EB%8F%99%EC%A0%84_(36%EC%9E%A5_%EC%99%84%ED%8C%90%EB%B3%B8))*, paired with a beautiful [modern translation](https://ko.wikisource.org/wiki/%EB%B2%88%EC%97%AD:%ED%99%8D%EA%B8%B8%EB%8F%99%EC%A0%84_(36%EC%9E%A5_%EC%99%84%ED%8C%90%EB%B3%B8)) by `직지프로` (licensed under Creative Commons).

To make Gemma feel at home, I structured the data into a conversation, guiding the model with a clear `system` prompt:

```json
[
  {"role": "system", "content": "Translate Classical Korean into Modern Korean."},
  {"role": "user", "content": "됴션국셰둉ᄃᆡ왕즉위십오연의홍희문밧긔ᄒᆞᆫᄌᆡ상이잇스되"},
  {"role": "assistant", "content": "조선국 세종대왕 즉위 십오년에 홍회문 밖에 한 재상이 있으되,"}
]
```

> *(Translation note: This line introduces us to a prime minister living just outside the Honghoemun Gate during the 15th year of King Sejong's reign!)*

# The "Before" Picture

Before giving Gemma any specific training, I ran a quick baseline test. Base models are smart, but archaic grammar is a highly specific domain. Without tuning, Gemma tried its best but ended up giving long, overly literal explanations:

* **Original Classical Text:** ᄇᆡᆨ씨듯고ᄂᆡ심의탄복왈그근본을ᄀᆞᆷ초지아니ᄒᆞ니장부로다ᄒᆞ고ᄌᆡ삼위로ᄒᆞ더라
* **Human Translation:** 백씨 듣고 내심에 탄복 왈, "그 근본을 감추지 아니하니 장부로다!" 하고, 재삼 위로하더라.
* **Gemma's Initial Guess:** *"Like the color, the heart's praise said, 'The foundation cannot be deeply felt...'"*
* **Initial Similarity Score:** **4.85%** 💔

> *(Translation note: This line actually means - Upon hearing this, Mr. Baek was deeply impressed and said, "He does not hide his true nature; he is a true man!" and comforted him again and again.)*

The base model was clearly lost in time. It needed a map.

# Teaching Gemma with Care

To train the model efficiently, I used a Parameter-Efficient Fine-Tuning (PEFT) setup with LoRA.

```python
from peft import LoraConfig

peft_config = LoraConfig(
    lora_alpha=16,
    lora_dropout=0.05,
    r=16,
    bias="none",
    target_modules="all-linear",
    task_type="CAUSAL_LM",
)
```

**The Secret Sauce: `collate_fn`**

When fine-tuning a chat model to behave like a specific tool, you don't want it to waste energy learning how to re-write your prompt. By using a custom data collator, I masked the `system` and `user` inputs (setting their labels to `-100`), forcing Gemma's loss calculation to focus *strictly* on generating the correct modern assistant response.

After setting our hyper-parameters to gently cruise through 5 epochs with a learning rate of `2e-5`, I hit train.

# The Warm "After" Glow

After a bit of patience and letting the trainer do its magic, the results were incredibly rewarding. The character-by-character similarity score jumped all the way up to a brilliant **79.93%**!

Look at how it handles the text now:

* **Original Classical Text:** ᄇᆡᆨ씨듯고ᄂᆡ심의탄복왈그근본을ᄀᆞᆷ초지아니ᄒᆞ니장부로다ᄒᆞ고ᄌᆡ삼위로ᄒᆞ더라
* **Human Translation:** 백씨 듣고 내심에 탄복 왈, "그 근본을 감추지 아니하니 장부로다!" 하고, 재삼 위로하더라.
* **Gemma's Fine-Tuned Translation:** 백씨듯 고내심에 탄복 왈, "그 근본을 감초지 아니하니 장부로다." 하고 제삼 위로 하더라.
* **New Similarity Score:** **85.71%** ✨

# Closing Thoughts

Technology often pushes us relentlessly into the future, but my favorite tech projects are the ones that allow us to look backward with greater clarity. By spending a little time fine-tuning a lightweight model like Gemma 4, we can build tools that preserve cultural history, making ancient wisdom and classic stories accessible to anyone with a laptop.

Next time you find a piece of history that feels just a bit too out of reach, remember that a small dataset and a fine-tuning session might be all you need to bring it into the light.

Here's the structured workflow when you do a fine-tuning for your own domain:

1. Define a clear goal
2. Prepare a high-quality dataset and evaluation plan
3. Verify the model is learning
4. Evaluate with metrics and human judgment
5. Deploy and iterate

👉 [Check out this tutorial in Gemma Cookbook](https://colab.research.google.com/github/google-gemma/cookbook/blob/main/tutorials/Translator_of_Old_Korean_Literature.ipynb)\
👉 [Star the repository to support us](https://github.com/google-gemma/cookbook)
