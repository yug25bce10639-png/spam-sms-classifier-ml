% Prolog based spam detection using simple rules

% Define spam keywords
spam_keyword(win).
spam_keyword(free).
spam_keyword(prize).
spam_keyword(money).
spam_keyword(lottery).
spam_keyword(offer).

% Rule to check if a message contains spam keyword
is_spam(Message) :-
    spam_keyword(Word),
    sub_atom(Message, _, _, _, Word).

% Rule for non-spam
is_not_spam(Message) :-
    \+ is_spam(Message).
