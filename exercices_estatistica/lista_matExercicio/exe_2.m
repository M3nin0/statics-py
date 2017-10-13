% Exercício 2

% Calcule a média de notas de uma sala de 40 alunos
% Processo realizado passo-a-passo

% Notas
% Quantidade - nota
% 1 - 2
% 4 - 3
% 4 - 4
% 6 - 5
% 5 - 6
% 8 - 7
% 8 - 8
% 4 - 9

clear all;

alunos = [1, 4, 4, 6, 5 , 8, 8, 4];
notas = [2, 3, 4, 5, 6, 7, 8, 9];

mediaP = 0;
mediaP = (alunos(1) * notas(1)) + mediaP;
mediaP = (alunos(2) * notas(2)) + mediaP;
mediaP = (alunos(3) * notas(3)) + mediaP;
mediaP = (alunos(4) * notas(4)) + mediaP;
mediaP = (alunos(5) * notas(5)) + mediaP;
mediaP = (alunos(6) * notas(6)) + mediaP;
mediaP = (alunos(7) * notas(7)) + mediaP;
mediaP = (alunos(8) * notas(8)) + mediaP;

media = mediaP / 40;

disp(media)