"""Tests for gene product color handling."""

from loica.geneproduct import GeneProduct, Regulator, Reporter


def test_gene_product_accepts_hex_color():
    gene_product = GeneProduct("gfp", color="#00FF00")

    assert gene_product.color == "#00FF00"


def test_regulator_accepts_hex_color():
    regulator = Regulator("lacI", color="#1A2B3C")

    assert regulator.color == "#1A2B3C"


def test_reporter_accepts_hex_color():
    reporter = Reporter("rfp", color="#FF0000")

    assert reporter.color == "#FF0000"
