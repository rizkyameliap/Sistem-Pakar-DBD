% GEJALA PENYAKIT DBD (Demam Berdarah Dengue)
% DATABASE

%-- Menyimpan data apakah gejala X positif atau negatif.
:- dynamic gejala_pos/1.
:- dynamic gejala_neg/1.

% ATURAN
%-- Predikat pertanyaan/1 untuk menanyakan pertanyaan terkait gejala X.
pertanyaan(demam_tinggi) :-
    write("Apakah Anda mengalami demam tinggi?").
pertanyaan(nyeri_otot) :-
    write("Apakah Anda merasa nyeri otot?").
pertanyaan(nyeri_sendi) :-
    write("Apakah Anda merasa nyeri sendi?").
pertanyaan(sakit_kepala) :-
    write("Apakah Anda sakit kepala?").
pertanyaan(mual) :-
    write("Apakah Anda merasa mual atau muntah?").
pertanyaan(nyeri_perut) :-
    write("Apakah Anda merasa nyeri di perut?").
pertanyaan(bintik_merah) :-
    write("Apakah muncul bintik merah di kulit Anda?").

%-- Predikat diagnosa/1 digunakan untuk menanyakan dan menyimpan status gejala X.
diagnosa(G) :-
    pertanyaan(G),
    writeln(" (y/t)"),
    read(Jawaban),
    Jawaban == y,
    assertz(gejala_pos(G)).
diagnosa(G) :-
    assertz(gejala_neg(G)),
    fail.

%-- Predikat gejala/1 dipanggil untuk memeriksa status gejala dari database
gejala(G) :-
    gejala_pos(G), !.
gejala(G) :-
    gejala_neg(G), !,
    fail.
gejala(G) :-
    diagnosa(G).

%-- Daftar gejala khas penyakit DBD
penyakit(dbd) :-
    gejala(demam_tinggi),
    gejala(nyeri_otot),
    gejala(nyeri_sendi),
    gejala(sakit_kepala),
    gejala(bintik_merah),
    terdeteksi("Demam Berdarah (DBD)").

%-- Jika tidak ada yang cocok
penyakit(_) :-
    writeln("Tidak terdeteksi penyakit.").

%-- Predikat untuk mencetak penyakit yang terdeteksi
terdeteksi(P) :-
    write("Anda terdeteksi penyakit "),
    writeln(P).

%-- Predikat untuk membersihkan database gejala
clear_db :-
    retractall(gejala_pos(_)),
    retractall(gejala_neg(_)).

%-- Main loop sistem pakar
main :-
    write('\33\[2J'), % Clear screen
    writeln("DIAGNOSA PENYAKIT DBD"),
    penyakit(_),
    clear_db,
    writeln("INGIN MENGULANG?"),
    read(Jawaban), !,
    Jawaban == y,
    main.
