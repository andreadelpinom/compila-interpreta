factorial(0, 1).  % Caso base: el factorial de 0 es 1
factorial(N, R) :-
    N > 0,            % Asegura que N sea mayor que 0
    N1 is N - 1,      % Calcula N - 1
    factorial(N1, R1),  % Llama recursivamente para calcular factorial de N1
    R is N * R1.      % R es el producto de N y el factorial de N1


