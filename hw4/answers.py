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


"""

part1_q2 = r"""
**Your answer:**


"""

part1_q3 = r"""
**Your answer:**


"""

part1_q4 = r"""
**Your answer:**


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


"""

part2_q2 = r"""
**Your answer:**


"""


# ==============
