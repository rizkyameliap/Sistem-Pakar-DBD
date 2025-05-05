% GEJALA PENYAKIT DBD
% DATABASE
:- dynamic gejala_pos/1.
:- dynamic gejala_neg/1.

% FAKTA PENYAKIT DBD
penyakit("DBD Ringan").
penyakit("DBD Sedang").
penyakit("DBD Berat").

% GEJALA-GEJALA UNTUK MASING-MASING TINGKAT DBD
gejala(demam_tinggi, "DBD Ringan").
gejala(nyeri_otot, "DBD Ringan").
gejala(nyeri_sendi, "DBD Ringan").

gejala(sakit_kepala, "DBD Sedang").
gejala(mual, "DBD Sedang").
gejala(nyeri_perut, "DBD Sedang").

gejala(bintik_merah, "DBD Berat").
gejala(mimisan, "DBD Berat").
gejala(pendarahan_gusi, "DBD Berat").

% PERTANYAAN UNTUK MASING-MASING GEJALA
pertanyaan(demam_tinggi, Y) :-
    Y = "Apakah Anda mengalami demam tinggi?".
pertanyaan(nyeri_otot, Y) :-
    Y = "Apakah Anda merasa nyeri otot?".
pertanyaan(nyeri_sendi, Y) :-
    Y = "Apakah Anda merasa nyeri sendi?".
pertanyaan(sakit_kepala, Y) :-
    Y = "Apakah Anda sering sakit kepala?".
pertanyaan(mual, Y) :-
    Y = "Apakah Anda merasa mual atau muntah?".
pertanyaan(nyeri_perut, Y) :-
    Y = "Apakah Anda merasakan nyeri di bagian perut?".
pertanyaan(bintik_merah, Y) :-
    Y = "Apakah muncul bintik-bintik merah pada kulit Anda?".
pertanyaan(mimisan, Y) :-
    Y = "Apakah Anda mengalami mimisan?".
pertanyaan(pendarahan_gusi, Y) :-
    Y = "Apakah gusi Anda berdarah?".
