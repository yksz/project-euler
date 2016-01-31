%% If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
%% Find the sum of all the multiples of 3 or 5 below 1000.

-module(problem1).
-export([main/0]).

sum(L) -> sum(L, 0).
sum([], N) -> N;
sum([H|T], N) -> sum(T, H+N).

main() ->
    Pred = fun(X) ->
               if
                   X rem 3 =:= 0 -> true;
                   X rem 5 =:= 0 -> true;
                   true -> false
               end
           end,
    L = lists:filter(Pred, lists:seq(1, 999)),
    io:format(integer_to_list(sum(L))).
