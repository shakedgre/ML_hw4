r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""

import os

# ==============
# Dataset location
#
# Root directory containing the pre-prepared dataset files used by the
# notebooks (e.g. the `hw4_tests/` directory used to verify your
# implementation). Change this to point to wherever you placed the datasets
# on the course HPC.
DATASETS_DIR = os.path.expanduser("~/datasets")

# ==============
# Part 1 answers


def part1_rnn_hyperparams():
    hypers = dict(
        batch_size=0,
        seq_len=0,
        h_dim=0,
        n_layers=0,
        dropout=0,
        learn_rate=0.0,
        lr_sched_factor=0.0,
        lr_sched_patience=0,
    )
    # TODO: Set the hyperparameters to train the model.
    # ====== YOUR CODE: ======
    hypers.update(
        batch_size=64,
        seq_len=64,
        h_dim=256,
        n_layers=3,
        dropout=0.2,
        learn_rate=1e-3,
        lr_sched_factor=0.5,
        lr_sched_patience=2,
    )
    # ========================
    return hypers


def part1_generation_params():
    start_seq = ""
    temperature = 0.0001
    # TODO: Tweak the parameters to generate a literary masterpiece.
    # ====== YOUR CODE: ======
    start_seq = "ACT I."
    temperature = 0.5
    # ========================
    return start_seq, temperature


part1_q1 = r"""
**Your answer:**

We split the corpus into fixed-length sequences because training on the whole text as one sequence would be too expensive in memory and computation, and backpropagation through the entire corpus would create an extremely long computation graph. Shorter sequences let us train with mini-batches and truncated backpropagation through time. The model still learns local sequential structure, while the hidden state can carry information between adjacent batches when the sampler preserves their order.
"""

part1_q2 = r"""
**Your answer:**

Even though gradients are only propagated through one sequence at a time, the recurrent hidden state is passed from one sequence to the next during generation, and during training when batches are ordered correctly. That hidden state is a learned summary of previous characters, so information from earlier text can influence later predictions. The sequence length limits how far gradients are directly backpropagated, not how long the hidden state can be carried forward at inference time.
"""

part1_q3 = r"""
**Your answer:**

We do not shuffle batches because the RNN hidden state is meant to continue from one batch to the next. The custom sampler arranges batches so that samples in the same batch position are consecutive chunks of the corpus across adjacent batches. If we shuffled, the hidden state from one text segment would be reused for an unrelated segment, which would corrupt the temporal continuity and make stateful training incorrect.
"""

part1_q4 = r"""
**Your answer:**

We lower the sampling temperature to make the generated text less random and more likely to follow the high-probability character patterns learned by the model.

When the temperature is very high, the logits are flattened before softmax, so the probability distribution becomes closer to uniform. The model then samples many unlikely characters, which usually produces noisy, incoherent text.

When the temperature is very low, the largest logit dominates the softmax, so sampling becomes almost deterministic. This can improve spelling and local structure, but if it is too low the output becomes repetitive and can get stuck in common loops.
"""
# ==============


# ==============
# Part 2 answers

PART2_CUSTOM_DATA_URL = None


def part2_transformer_encoder_hyperparams():
    hypers = dict(
        embed_dim = 0, 
        num_heads = 0,
        num_layers = 0,
        hidden_dim = 0,
        window_size = 0,
        droupout = 0.0,
        lr=0.0,
    )

    # TODO: Tweak the hyperparameters to train the transformer encoder.
    # ====== YOUR CODE: ======
    hypers.update(
        embed_dim=64,
        num_heads=4,
        num_layers=2,
        hidden_dim=128,
        window_size=16,
        droupout=0.1,
        lr=1e-3,
    )
    # ========================
    return hypers




part2_q1 = r"""
**Your answer:**

Each sliding-window attention layer lets a token mix information only from nearby tokens inside its window. After one layer, a token representation contains information from its local neighborhood. After a second layer, neighboring tokens already contain information from their own neighborhoods, so the token indirectly receives information from a wider region. Stacking layers therefore expands the effective receptive field, similar to how stacked convolution layers cover a larger part of an image even when each kernel is small.
"""

part2_q2 = r"""
**Your answer:**

One useful variation is to combine local sliding-window attention with a small set of global tokens. For example, the CLS token and maybe a few selected summary tokens can attend to all positions, while regular tokens attend to their local window plus those global tokens. This keeps the cost close to O(nw) when the number of global tokens is small, but it gives every position a short path to information from the whole sequence through the global tokens.
"""


# ==============
