annotation-target::comp programming handbook.pdf






>%%
>```annotation-json
>{"created":"2024-12-04T20:18:56.135Z","text":"Cool way of getting the input and output to be faster ","updated":"2024-12-04T20:18:56.135Z","document":{"title":"comp programming handbook.pdf","link":[{"href":"urn:x-pdf:a37d3c066bae434ae0996e9fbfbcca24"},{"href":"vault:/book notes/books/comp programming handbook.pdf"}],"documentFingerprint":"a37d3c066bae434ae0996e9fbfbcca24"},"uri":"vault:/book notes/books/comp programming handbook.pdf","target":[{"source":"vault:/book notes/books/comp programming handbook.pdf","selector":[{"type":"TextPositionSelector","start":15903,"end":16045},{"type":"TextQuoteSelector","exact":"nput and output is sometimes a bottleneck in the program. The followinglines at the beginning of the code make input and output more efficient","prefix":"< \" \" << b << \" \" << x << \"\\n\";I","suffix":":ios::sync_with_stdio(0);cin.tie"}]}]}
>```
>%%
>*%%PREFIX%%< " " << b << " " << x << "\n";I%%HIGHLIGHT%% ==nput and output is sometimes a bottleneck in the program. The followinglines at the beginning of the code make input and output more efficient== %%POSTFIX%%:ios::sync_with_stdio(0);cin.tie*
>%%LINK%%[[#^wq71q3if7k|show annotation]]
>%%COMMENT%%
>Cool way of getting the input and output to be faster 
>%%TAGS%%
>
^wq71q3if7k




>%%
>```annotation-json
>{"created":"2024-12-04T20:21:21.345Z","text":"Int: 2^31 or 2 * 10^9 \nLong: 2^63 or 9 * 10^18 ","updated":"2024-12-04T20:21:21.345Z","document":{"title":"comp programming handbook.pdf","link":[{"href":"urn:x-pdf:a37d3c066bae434ae0996e9fbfbcca24"},{"href":"vault:/book notes/books/comp programming handbook.pdf"}],"documentFingerprint":"a37d3c066bae434ae0996e9fbfbcca24"},"uri":"vault:/book notes/books/comp programming handbook.pdf","target":[{"source":"vault:/book notes/books/comp programming handbook.pdf","selector":[{"type":"TextPositionSelector","start":17270,"end":17567},{"type":"TextQuoteSelector","exact":"The most used integer type in competitive programming is int, which is a 32-bittype with a value range of −231 . . . 231 −1 or about −2 ·109 . . . 2 ·109. If the typeint is not enough, the 64-bit type long long can be used. It has a value range of−263 . . . 263 −1 or about −9 ·1018 . . . 9 ·1018.","prefix":"xt”.Working with numbersIntegers","suffix":"The following code defines a lon"}]}]}
>```
>%%
>*%%PREFIX%%xt”.Working with numbersIntegers%%HIGHLIGHT%% ==The most used integer type in competitive programming is int, which is a 32-bittype with a value range of −231 . . . 231 −1 or about −2 ·109 . . . 2 ·109. If the typeint is not enough, the 64-bit type long long can be used. It has a value range of−263 . . . 263 −1 or about −9 ·1018 . . . 9 ·1018.== %%POSTFIX%%The following code defines a lon*
>%%LINK%%[[#^57cgc7lsh4m|show annotation]]
>%%COMMENT%%
>Int: 2^31 or 2 * 10^9 
>Long: 2^63 or 9 * 10^18 
>%%TAGS%%
>
^57cgc7lsh4m


>%%
>```annotation-json
>{"created":"2024-12-04T20:24:57.863Z","updated":"2024-12-04T20:24:57.863Z","document":{"title":"comp programming handbook.pdf","link":[{"href":"urn:x-pdf:a37d3c066bae434ae0996e9fbfbcca24"},{"href":"vault:/book notes/books/comp programming handbook.pdf"}],"documentFingerprint":"a37d3c066bae434ae0996e9fbfbcca24"},"uri":"vault:/book notes/books/comp programming handbook.pdf","target":[{"source":"vault:/book notes/books/comp programming handbook.pdf","selector":[{"type":"TextPositionSelector","start":18349,"end":18394},{"type":"TextQuoteSelector","exact":"the g++ compiler also provides a 128-bit type","prefix":". Still,it is good to know that ","suffix":" __int128_twith a value range of"}]}]}
>```
>%%
>*%%PREFIX%%. Still,it is good to know that %%HIGHLIGHT%% ==the g++ compiler also provides a 128-bit type== %%POSTFIX%%__int128_twith a value range of*
>%%LINK%%[[#^402455bko88|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^402455bko88


>%%
>```annotation-json
>{"created":"2024-12-04T20:26:28.144Z","updated":"2024-12-04T20:26:28.144Z","document":{"title":"comp programming handbook.pdf","link":[{"href":"urn:x-pdf:a37d3c066bae434ae0996e9fbfbcca24"},{"href":"vault:/book notes/books/comp programming handbook.pdf"}],"documentFingerprint":"a37d3c066bae434ae0996e9fbfbcca24"},"uri":"vault:/book notes/books/comp programming handbook.pdf","target":[{"source":"vault:/book notes/books/comp programming handbook.pdf","selector":[{"type":"TextPositionSelector","start":18621,"end":18653},{"type":"TextQuoteSelector","exact":"17 mod 5 =2, because 17 =3 ·5 +2","prefix":" x is divided by m. For example,","suffix":".Sometimes, the answer to a prob"}]}]}
>```
>%%
>*%%PREFIX%%x is divided by m. For example,%%HIGHLIGHT%% ==17 mod 5 =2, because 17 =3 ·5 +2== %%POSTFIX%%.Sometimes, the answer to a prob*
>%%LINK%%[[#^3mkhepkdtry|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^3mkhepkdtry



>%%
>```annotation-json
>{"created":"2024-12-04T20:41:04.887Z","text":"I wonder why? ","updated":"2024-12-04T20:41:04.887Z","document":{"title":"comp programming handbook.pdf","link":[{"href":"urn:x-pdf:a37d3c066bae434ae0996e9fbfbcca24"},{"href":"vault:/book notes/books/comp programming handbook.pdf"}],"documentFingerprint":"a37d3c066bae434ae0996e9fbfbcca24"},"uri":"vault:/book notes/books/comp programming handbook.pdf","target":[{"source":"vault:/book notes/books/comp programming handbook.pdf","selector":[{"type":"TextPositionSelector","start":19449,"end":19512},{"type":"TextQuoteSelector","exact":"Usually we want the remainder to always be between 0 . . . m −1","prefix":" = (x*i)%m;}cout << x%m << \"\\n\";","suffix":". However, inC++ and other langu"}]}]}
>```
>%%
>*%%PREFIX%%= (x*i)%m;}cout << x%m << "\n";%%HIGHLIGHT%% ==Usually we want the remainder to always be between 0 . . . m −1== %%POSTFIX%%. However, inC++ and other langu*
>%%LINK%%[[#^1kvnbgdao8x|show annotation]]
>%%COMMENT%%
>I wonder why? 
>%%TAGS%%
>
^1kvnbgdao8x


>%%
>```annotation-json
>{"created":"2024-12-04T20:41:29.447Z","text":"Neat little trick ","updated":"2024-12-04T20:41:29.447Z","document":{"title":"comp programming handbook.pdf","link":[{"href":"urn:x-pdf:a37d3c066bae434ae0996e9fbfbcca24"},{"href":"vault:/book notes/books/comp programming handbook.pdf"}],"documentFingerprint":"a37d3c066bae434ae0996e9fbfbcca24"},"uri":"vault:/book notes/books/comp programming handbook.pdf","target":[{"source":"vault:/book notes/books/comp programming handbook.pdf","selector":[{"type":"TextPositionSelector","start":19612,"end":19755},{"type":"TextQuoteSelector","exact":"An easy way to make sure there are no negative remainders is to firstcalculate the remainder as usual and then add m if the result is negative:","prefix":"mber is either zero ornegative. ","suffix":"x = x%m;if (x < 0) x += m;Howeve"}]}]}
>```
>%%
>*%%PREFIX%%mber is either zero ornegative.%%HIGHLIGHT%% ==An easy way to make sure there are no negative remainders is to firstcalculate the remainder as usual and then add m if the result is negative:== %%POSTFIX%%x = x%m;if (x < 0) x += m;Howeve*
>%%LINK%%[[#^nbn6d3pwut|show annotation]]
>%%COMMENT%%
>Neat little trick 
>%%TAGS%%
>
^nbn6d3pwut


>%%
>```annotation-json
>{"created":"2024-12-04T20:48:00.000Z","updated":"2024-12-04T20:48:00.000Z","document":{"title":"comp programming handbook.pdf","link":[{"href":"urn:x-pdf:a37d3c066bae434ae0996e9fbfbcca24"},{"href":"vault:/book notes/books/comp programming handbook.pdf"}],"documentFingerprint":"a37d3c066bae434ae0996e9fbfbcca24"},"uri":"vault:/book notes/books/comp programming handbook.pdf","target":[{"source":"vault:/book notes/books/comp programming handbook.pdf","selector":[{"type":"TextPositionSelector","start":20808,"end":20974},{"type":"TextQuoteSelector","exact":"It is risky to compare floating point numbers with the == operator, because itis possible that the values should be equal but they are not because of precisionerrors.","prefix":"ile the correctvalue would be 1.","suffix":" A better way to compare floatin"}]}]}
>```
>%%
>*%%PREFIX%%ile the correctvalue would be 1.%%HIGHLIGHT%% ==It is risky to compare floating point numbers with the == operator, because it is possible that the values should be equal but they are not because of precision errors.== %%POSTFIX%%A better way to compare floatin*
>%%LINK%%[[#^1f5hm3wtpkmi|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^1f5hm3wtpkmi


>%%
>```annotation-json
>{"created":"2024-12-04T21:09:03.025Z","text":"Good thing to keep in mind\n","updated":"2024-12-04T21:09:03.025Z","document":{"title":"comp programming handbook.pdf","link":[{"href":"urn:x-pdf:a37d3c066bae434ae0996e9fbfbcca24"},{"href":"vault:/book notes/books/comp programming handbook.pdf"}],"documentFingerprint":"a37d3c066bae434ae0996e9fbfbcca24"},"uri":"vault:/book notes/books/comp programming handbook.pdf","target":[{"source":"vault:/book notes/books/comp programming handbook.pdf","selector":[{"type":"TextPositionSelector","start":21487,"end":21694},{"type":"TextQuoteSelector","exact":"Short code is ideal in competitive programming, because programs should bewritten as fast as possible. Because of this, competitive programmers often defineshorter names for datatypes and other parts of code","prefix":"e is at most 253.Shortening code","suffix":".Type namesUsing the command typ"}]}]}
>```
>%%
>*%%PREFIX%%e is at most 253.Shortening code%%HIGHLIGHT%% ==Short code is ideal in competitive programming, because programs should bewritten as fast as possible. Because of this, competitive programmers often defineshorter names for datatypes and other parts of code== %%POSTFIX%%.Type namesUsing the command typ*
>%%LINK%%[[#^5ug7mf4msj4|show annotation]]
>%%COMMENT%%
>Good thing to keep in mind
>
>%%TAGS%%
>
^5ug7mf4msj4


>%%
>```annotation-json
>{"created":"2024-12-04T21:14:49.706Z","updated":"2024-12-04T21:14:49.706Z","document":{"title":"comp programming handbook.pdf","link":[{"href":"urn:x-pdf:a37d3c066bae434ae0996e9fbfbcca24"},{"href":"vault:/book notes/books/comp programming handbook.pdf"}],"documentFingerprint":"a37d3c066bae434ae0996e9fbfbcca24"},"uri":"vault:/book notes/books/comp programming handbook.pdf","target":[{"source":"vault:/book notes/books/comp programming handbook.pdf","selector":[{"type":"TextPositionSelector","start":22481,"end":22528},{"type":"TextQuoteSelector","exact":"For example, we can define the following macros","prefix":"fined using the #define keyword.","suffix":":#define F first#define S second"}]}]}
>```
>%%
>*%%PREFIX%%fined using the #define keyword.%%HIGHLIGHT%% ==For example, we can define the following macros== %%POSTFIX%%:#define F first#define S second*
>%%LINK%%[[#^iturnoxvhkf|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^iturnoxvhkf


>%%
>```annotation-json
>{"created":"2024-12-04T21:21:29.283Z","updated":"2024-12-04T21:21:29.283Z","document":{"title":"comp programming handbook.pdf","link":[{"href":"urn:x-pdf:a37d3c066bae434ae0996e9fbfbcca24"},{"href":"vault:/book notes/books/comp programming handbook.pdf"}],"documentFingerprint":"a37d3c066bae434ae0996e9fbfbcca24"},"uri":"vault:/book notes/books/comp programming handbook.pdf","target":[{"source":"vault:/book notes/books/comp programming handbook.pdf","selector":[{"type":"TextPositionSelector","start":24413,"end":24486},{"type":"TextQuoteSelector","exact":"The sum of an arithmetic progres-sion can be calculated using the formula","prefix":"ic progression with constant 4. ","suffix":"a +···+b︸ ︷︷ ︸n numbers= n(a +b)"}]}]}
>```
>%%
>*%%PREFIX%%ic progression with constant 4.%%HIGHLIGHT%% ==The sum of an arithmetic progres-sion can be calculated using the formula== %%POSTFIX%%a +···+b︸ ︷︷ ︸n numbers= n(a +b)*
>%%LINK%%[[#^lf8mlryn45m|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^lf8mlryn45m


>%%
>```annotation-json
>{"created":"2024-12-04T21:24:40.468Z","updated":"2024-12-04T21:24:40.468Z","document":{"title":"comp programming handbook.pdf","link":[{"href":"urn:x-pdf:a37d3c066bae434ae0996e9fbfbcca24"},{"href":"vault:/book notes/books/comp programming handbook.pdf"}],"documentFingerprint":"a37d3c066bae434ae0996e9fbfbcca24"},"uri":"vault:/book notes/books/comp programming handbook.pdf","target":[{"source":"vault:/book notes/books/comp programming handbook.pdf","selector":[{"type":"TextPositionSelector","start":24943,"end":25011},{"type":"TextQuoteSelector","exact":"he sum of a geometric progressioncan be calculated using the formula","prefix":"c progression with constant 2. T","suffix":"a +ak +ak2 +···+b = bk −ak −1whe"}]}]}
>```
>%%
>*%%PREFIX%%c progression with constant 2. T%%HIGHLIGHT%% ==he sum of a geometric progressioncan be calculated using the formula== %%POSTFIX%%a +ak +ak2 +···+b = bk −ak −1whe*
>%%LINK%%[[#^fqj5hx2wvfb|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^fqj5hx2wvfb


>%%
>```annotation-json
>{"created":"2024-12-04T21:27:18.154Z","text":"Another sum to keep mind of. ","updated":"2024-12-04T21:27:18.154Z","document":{"title":"comp programming handbook.pdf","link":[{"href":"urn:x-pdf:a37d3c066bae434ae0996e9fbfbcca24"},{"href":"vault:/book notes/books/comp programming handbook.pdf"}],"documentFingerprint":"a37d3c066bae434ae0996e9fbfbcca24"},"uri":"vault:/book notes/books/comp programming handbook.pdf","target":[{"source":"vault:/book notes/books/comp programming handbook.pdf","selector":[{"type":"TextPositionSelector","start":25460,"end":25495},{"type":"TextQuoteSelector","exact":"A harmonic sum is a sum of the form","prefix":"a1 +2 +4 +8 +. . . +2n−1 =2n −1.","suffix":"n∑x=11x =1 +12 +13 +. . . +1n .A"}]}]}
>```
>%%
>*%%PREFIX%%a1 +2 +4 +8 +. . . +2n−1 =2n −1.%%HIGHLIGHT%% ==A harmonic sum is a sum of the form== %%POSTFIX%%n∑x=11x =1 +12 +13 +. . . +1n .A*
>%%LINK%%[[#^lpvnizulx1m|show annotation]]
>%%COMMENT%%
>Another sum to keep mind of. 
>%%TAGS%%
>
^lpvnizulx1m


>%%
>```annotation-json
>{"created":"2024-12-04T21:28:09.806Z","text":"Good reminder of set theory ","updated":"2024-12-04T21:28:09.806Z","document":{"title":"comp programming handbook.pdf","link":[{"href":"urn:x-pdf:a37d3c066bae434ae0996e9fbfbcca24"},{"href":"vault:/book notes/books/comp programming handbook.pdf"}],"documentFingerprint":"a37d3c066bae434ae0996e9fbfbcca24"},"uri":"vault:/book notes/books/comp programming handbook.pdf","target":[{"source":"vault:/book notes/books/comp programming handbook.pdf","selector":[{"type":"TextPositionSelector","start":26040,"end":26110},{"type":"TextQuoteSelector","exact":"|S|denotesthe size of a set S, i.e., the number of elements in the set","prefix":"mbol ;denotes an empty set, and ","suffix":". For example, in theabove set, "}]}]}
>```
>%%
>*%%PREFIX%%mbol ;denotes an empty set, and%%HIGHLIGHT%% ==|S|denotesthe size of a set S, i.e., the number of elements in the set== %%POSTFIX%%. For example, in theabove set,*
>%%LINK%%[[#^rtntelrp2pk|show annotation]]
>%%COMMENT%%
>Good reminder of set theory 
>%%TAGS%%
>
^rtntelrp2pk


>%%
>```annotation-json
>{"created":"2024-12-04T21:29:16.703Z","text":"Good reminder of mathematical logic. ","updated":"2024-12-04T21:29:16.703Z","document":{"title":"comp programming handbook.pdf","link":[{"href":"urn:x-pdf:a37d3c066bae434ae0996e9fbfbcca24"},{"href":"vault:/book notes/books/comp programming handbook.pdf"}],"documentFingerprint":"a37d3c066bae434ae0996e9fbfbcca24"},"uri":"vault:/book notes/books/comp programming handbook.pdf","target":[{"source":"vault:/book notes/books/comp programming handbook.pdf","selector":[{"type":"TextPositionSelector","start":27751,"end":27996},{"type":"TextQuoteSelector","exact":"The value of a logical expression is either true (1) or false (0). The most impor-tant logical operators are ¬(negation), ∧(conjunction), ∨(disjunction), ⇒(implication) and ⇔(equivalence). The following table shows the meaningsof these operators","prefix":"ntains all even integers.12Logic","suffix":":A B ¬A ¬B A ∧B A ∨B A ⇒B A ⇔B0 "}]}]}
>```
>%%
>*%%PREFIX%%ntains all even integers.12Logic%%HIGHLIGHT%% ==The value of a logical expression is either true (1) or false (0). The most impor-tant logical operators are ¬(negation), ∧(conjunction), ∨(disjunction), ⇒(implication) and ⇔(equivalence). The following table shows the meaningsof these operators== %%POSTFIX%%:A B ¬A ¬B A ∧B A ∨B A ⇒B A ⇔B0*
>%%LINK%%[[#^qyhktyrzveb|show annotation]]
>%%COMMENT%%
>Good reminder of mathematical logic. 
>%%TAGS%%
>
^qyhktyrzveb


>%%
>```annotation-json
>{"created":"2024-12-04T21:32:13.101Z","text":"Super Good section about functions that are important ","updated":"2024-12-04T21:32:13.101Z","document":{"title":"comp programming handbook.pdf","link":[{"href":"urn:x-pdf:a37d3c066bae434ae0996e9fbfbcca24"},{"href":"vault:/book notes/books/comp programming handbook.pdf"}],"documentFingerprint":"a37d3c066bae434ae0996e9fbfbcca24"},"uri":"vault:/book notes/books/comp programming handbook.pdf","target":[{"source":"vault:/book notes/books/comp programming handbook.pdf","selector":[{"type":"TextPositionSelector","start":29322,"end":29456},{"type":"TextQuoteSelector","exact":"FunctionsThe function bxcrounds the number x down to an integer, and the function dxerounds the number x up to an integer. For example","prefix":"nis true in the set of integers.","suffix":",b3/2c=1 and d3/2e=2.The functio"}]}]}
>```
>%%
>*%%PREFIX%%nis true in the set of integers.%%HIGHLIGHT%% ==FunctionsThe function bxcrounds the number x down to an integer, and the function dxerounds the number x up to an integer. For example== %%POSTFIX%%,b3/2c=1 and d3/2e=2.The functio*
>%%LINK%%[[#^tzj33zkfg6|show annotation]]
>%%COMMENT%%
>Super Good section about functions that are important 
>%%TAGS%%
>
^tzj33zkfg6


>%%
>```annotation-json
>{"created":"2024-12-04T21:34:44.536Z","text":"Various Resources on different competitive programming contests (note these could eventually be outdated) ","updated":"2024-12-04T21:34:44.536Z","document":{"title":"comp programming handbook.pdf","link":[{"href":"urn:x-pdf:a37d3c066bae434ae0996e9fbfbcca24"},{"href":"vault:/book notes/books/comp programming handbook.pdf"}],"documentFingerprint":"a37d3c066bae434ae0996e9fbfbcca24"},"uri":"vault:/book notes/books/comp programming handbook.pdf","target":[{"source":"vault:/book notes/books/comp programming handbook.pdf","selector":[{"type":"TextPositionSelector","start":31256,"end":31278},{"type":"TextQuoteSelector","exact":"Contests and resources","prefix":"is 1111011 and blog2(123) +1c=7.","suffix":"IOIThe International Olympiad in"}]}]}
>```
>%%
>*%%PREFIX%%is 1111011 and blog2(123) +1c=7.%%HIGHLIGHT%% ==Contests and resources== %%POSTFIX%%IOIThe International Olympiad in*
>%%LINK%%[[#^wxo54q67q3o|show annotation]]
>%%COMMENT%%
>Various Resources on different competitive programming contests (note these could eventually be outdated) 
>%%TAGS%%
>
^wxo54q67q3o
