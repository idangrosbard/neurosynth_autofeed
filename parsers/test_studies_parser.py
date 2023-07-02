from . import StudiesParser
import pandas as pd


class TestStudiesParser:
    def test_compare_output(self):
        p = StudiesParser()
        inpt = '{"data": [["<a href=/studies/23146251/>Structural brain features of borderline personality and bipolar disorders.</a>","Rossi R, Pievani M, Lorenzi M, Boccardi M, Beneduce R, Bignotti S, Borsci G, Cotelli M, Giannakopoulos P, Magni LR, Rillosi L, Rosini S, Rossi G, Frisoni GB", "Psychiatry research", 1 ]]}'
        answer = p.parse(inpt)
        true_answer = pd.DataFrame({
            'Study': ['Structural brain features of borderline personality and bipolar disorders.'],
            'Authors': ['Rossi R, Pievani M, Lorenzi M, Boccardi M, Beneduce R, Bignotti S, Borsci G, Cotelli M, Giannakopoulos P, Magni LR, Rillosi L, Rosini S, Rossi G, Frisoni GB'],
            'Journal': ['Psychiatry research']
        })
        assert answer.equals(true_answer)
        
    def test_multiple_studies(self):
        p = StudiesParser()
        inpt = '{"data": [["<a href=/studies/23146251/>Structural brain features of borderline personality and bipolar disorders.</a>","Rossi R, Pievani M, Lorenzi M, Boccardi M, Beneduce R, Bignotti S, Borsci G, Cotelli M, Giannakopoulos P, Magni LR, Rillosi L, Rosini S, Rossi G, Frisoni GB", "Psychiatry research", 1 ],["<a href=/studies/21826762/>Effects of rapid eye movement sleep deprivation on fear extinction recall and prediction error signaling.</a>", "Spoormaker VI, Schroter MS, Andrade KC, Dresler M, Kiem SA, Goya-Maldonado R, Wetter TC, Holsboer F, Samann PG, Czisch M", "Human brain mapping", 1]]}'
        answer = p.parse(inpt)
        true_answer = pd.DataFrame({
            'Study': ['Structural brain features of borderline personality and bipolar disorders.', 'Effects of rapid eye movement sleep deprivation on fear extinction recall and prediction error signaling.'],
            'Authors': ['Rossi R, Pievani M, Lorenzi M, Boccardi M, Beneduce R, Bignotti S, Borsci G, Cotelli M, Giannakopoulos P, Magni LR, Rillosi L, Rosini S, Rossi G, Frisoni GB', 'Spoormaker VI, Schroter MS, Andrade KC, Dresler M, Kiem SA, Goya-Maldonado R, Wetter TC, Holsboer F, Samann PG, Czisch M'],
            'Journal': ['Psychiatry research', 'Human brain mapping']
        })
        assert answer.equals(true_answer)