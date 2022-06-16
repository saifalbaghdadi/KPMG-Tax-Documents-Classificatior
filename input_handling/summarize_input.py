import transformers
import pandas as pd
import os
import shutil


undisputed_best_model = transformers.MBartForConditionalGeneration.from_pretrained(
"ml6team/mbart-large-cc25-cnn-dailymail-nl-finetune"
)

tokenizer = transformers.MBartTokenizer.from_pretrained("facebook/mbart-large-cc25")


def summarize(text):
    
    summarization_pipeline = transformers.pipeline(
        task="summarization",
        model=undisputed_best_model,
        tokenizer=tokenizer,
    )
    summarization_pipeline.model.config.decoder_start_token_id = tokenizer.lang_code_to_id[
        "nl_XX"
    ]
    article = text  # Dutch
    summary = summarization_pipeline(
        article,
        do_sample=True,
        top_p=0.75,
        top_k=50,
        # num_beams=4,
        min_length=50,
        early_stopping=True,
        truncation=True,
    )[0]["summary_text"]

    
    return summary