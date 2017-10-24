% Interpolação - 1
% O número de bactérias por unidade de volume existente em uma cultura após
% X horas é apresentado na tabela
% 
% (x) n° de horas                            | 0  | 1  | 2  | 3  |  4  |
% (y) n° de bácterias por unidade de volume  | 32 | 47 | 65 | 92 | 132 |

% 1° Passo
% Definir os pontos que serão utilizados
p1 = [3, 92];
p2 = [4, 132];

%% Calcula o sistema de equação
a1 = -1 * p1(2);
b1 = p1(1);
c1 = 0;
a2 = p2(2);
b2 = p1(1);
c2 = 0;

%%
% Encontra a1
aF = a1 + a2;
% Encontra a2
a0 = P(p1, aF);

% Acha resultado
final = base(3.7, aF, a0);

disp('Resultado') 
disp(final)
