% 3-) Em  cada  bimestre,  uma faculdade  exige  a  realização  de  quatro  tipos 
% de  avaliação,  calculando  a  nota  bimestral pela média ponderada dessas avaliações. Se 
% a tabela apresenta as notas obtidas por uma aluna    nos    quatro    tipos    de    avali
% ações realizadas e os pesos dessas avaliações, sua nota bimenstral foi
% aproximandamente igual a

% As notas da escola e seus pesos
% Avaliação               Nota    Peso
% Prova escrita           6.0      4
% Avaliação continuada    7.0      4
% Seminário               8.0      2
% Trabalho em grupo       9.0      2

clear all;

notas = [6, 7, 8, 9];
peso = [4, 4, 2, 2];

p = 0
for x = 1:size(notas,2)
   p = (notas(x) * peso(x)) + p;
end

media = p / 12 % A divisão é feita pela soma de todos os pesos

disp(media)