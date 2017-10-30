function final = P2(t, p1, p2)

    % Sistema de equação
    a1 = -1 * p1(2);
    a2 = p2(2);
   
    % Encontra a1
    aF = a1 + a2;
    % Encontra a2
    a0 = P(p1, aF);

    % Acha resultado
    final = base(t, aF, a0);  
    
end
