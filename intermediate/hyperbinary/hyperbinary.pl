
% bintern(NumDigits, Value, Digits) is true if and only if Digits is a 
% bina-ternary representation of value, and is NumDigits long or less

% Base case for recursion
hyperbinary(0, 0, []).

hyperbinary(D, V, [N|Ns]) :- 
    D > 0,                  % Digits have to be more than 0
    V >= 0,                 % Value have to be more than 0 
    V =< 2**(D + 1),     % Value can't be any bigger than this
    member(N, [0, 1, 2]),   % Leftmost digit is one of [0, 1, 2]
    D2 is D - 1,            
    V2 is V - N*(2**(D-1)),
    hyperbinary(D2, V2, Ns).    % Recurse with new values for Digits and Value
