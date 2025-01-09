---
~
---
annotation-target::cs271 6th edition version.pdf


>%%
>```annotation-json
>{"created":"2025-01-07T23:05:38.617Z","updated":"2025-01-07T23:05:38.617Z","document":{"title":"Assembly Language for x86 Processors (Sixth edition)","link":[{"href":"urn:x-pdf:72d08f931fa25ac84e2dfc8557061efb"},{"href":"vault:/book notes/book pdfs /cs271 6th edition version.pdf"}],"documentFingerprint":"72d08f931fa25ac84e2dfc8557061efb"},"uri":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","target":[{"source":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","selector":[{"type":"TextPositionSelector","start":55373,"end":55375},{"type":"TextQuoteSelector","exact":"12","prefix":"ting large application programs?","suffix":". Challenge:  Translate the foll"}]}]}
>```
>%%
>*%%PREFIX%%ting large application programs?%%HIGHLIGHT%% ==12== %%POSTFIX%%. Challenge:  Translate the foll*
>%%LINK%%[[#^3s4wy6a739i|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^3s4wy6a739i


>%%
>```annotation-json
>{"created":"2025-01-07T23:12:01.239Z","updated":"2025-01-07T23:12:01.239Z","document":{"title":"Assembly Language for x86 Processors (Sixth edition)","link":[{"href":"urn:x-pdf:72d08f931fa25ac84e2dfc8557061efb"},{"href":"vault:/book notes/book pdfs /cs271 6th edition version.pdf"}],"documentFingerprint":"72d08f931fa25ac84e2dfc8557061efb"},"uri":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","target":[{"source":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","selector":[{"type":"TextPositionSelector","start":55936,"end":56199},{"type":"TextQuoteSelector","exact":"A  computer  can  usually  execute  programs  written  in  its  native   machine  language .  Eachinstruction in this language is simple enough to be executed using a relatively small number ofelectronic circuits. For simplicity, we will call this language   L0 .","prefix":" a computer, executing programs.","suffix":" Programmers  would  have  a  di"}]}]}
>```
>%%
>*%%PREFIX%%a computer, executing programs.%%HIGHLIGHT%% ==A  computer  can  usually  execute  programs  written  in  its  native   machine  language .  Eachinstruction in this language is simple enough to be executed using a relatively small number ofelectronic circuits. For simplicity, we will call this language   L0 .== %%POSTFIX%%Programmers  would  have  a  di*
>%%LINK%%[[#^56lcgmuva9|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^56lcgmuva9


>%%
>```annotation-json
>{"created":"2025-01-09T00:34:50.269Z","text":"Interpreted languages such as python and javascript which don't compile ","updated":"2025-01-09T00:34:50.269Z","document":{"title":"Assembly Language for x86 Processors (Sixth edition)","link":[{"href":"urn:x-pdf:72d08f931fa25ac84e2dfc8557061efb"},{"href":"vault:/book notes/book pdfs /cs271 6th edition version.pdf"}],"documentFingerprint":"72d08f931fa25ac84e2dfc8557061efb"},"uri":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","target":[{"source":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","selector":[{"type":"TextPositionSelector","start":56481,"end":56495},{"type":"TextQuoteSelector","exact":"Interpretation","prefix":"are two ways to achieve this: • ","suffix":":  As the L1 program is running,"}]}]}
>```
>%%
>*%%PREFIX%%are two ways to achieve this: •%%HIGHLIGHT%% ==Interpretation== %%POSTFIX%%:  As the L1 program is running,*
>%%LINK%%[[#^5dwo2s8t5iy|show annotation]]
>%%COMMENT%%
>Interpreted languages such as python and javascript which don't compile 
>%%TAGS%%
>
^5dwo2s8t5iy


>%%
>```annotation-json
>{"created":"2025-01-09T00:34:53.099Z","text":"basically a language using compilers. ","updated":"2025-01-09T00:34:53.099Z","document":{"title":"Assembly Language for x86 Processors (Sixth edition)","link":[{"href":"urn:x-pdf:72d08f931fa25ac84e2dfc8557061efb"},{"href":"vault:/book notes/book pdfs /cs271 6th edition version.pdf"}],"documentFingerprint":"72d08f931fa25ac84e2dfc8557061efb"},"uri":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","target":[{"source":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","selector":[{"type":"TextPositionSelector","start":56725,"end":56736},{"type":"TextQuoteSelector","exact":"Translation","prefix":"ecoded before it can execute. • ","suffix":":  The entire L1 program could b"}]}]}
>```
>%%
>*%%PREFIX%%ecoded before it can execute. •%%HIGHLIGHT%% ==Translation== %%POSTFIX%%:  The entire L1 program could b*
>%%LINK%%[[#^dfvcuu6pf4d|show annotation]]
>%%COMMENT%%
>basically a language using compilers. 
>%%TAGS%%
>
^dfvcuu6pf4d


>%%
>```annotation-json
>{"created":"2025-01-09T00:44:50.265Z","text":"Is this why architecture's are so different? ","updated":"2025-01-09T00:44:50.265Z","document":{"title":"Assembly Language for x86 Processors (Sixth edition)","link":[{"href":"urn:x-pdf:72d08f931fa25ac84e2dfc8557061efb"},{"href":"vault:/book notes/book pdfs /cs271 6th edition version.pdf"}],"documentFingerprint":"72d08f931fa25ac84e2dfc8557061efb"},"uri":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","target":[{"source":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","selector":[{"type":"TextPositionSelector","start":57801,"end":57923},{"type":"TextQuoteSelector","exact":"Machine VM1 cannot be radically different from VM0 because the translation or interpreta-tion would be too time-consuming.","prefix":"ted and executed on machine VM0.","suffix":" What if the language VM1 suppor"}]}]}
>```
>%%
>*%%PREFIX%%ted and executed on machine VM0.%%HIGHLIGHT%% ==Machine VM1 cannot be radically different from VM0 because the translation or interpreta-tion would be too time-consuming.== %%POSTFIX%%What if the language VM1 suppor*
>%%LINK%%[[#^m5vonn1gjhk|show annotation]]
>%%COMMENT%%
>Is this why architecture's are so different? 
>%%TAGS%%
>
^m5vonn1gjhk


>%%
>```annotation-json
>{"created":"2025-01-09T00:45:16.641Z","text":"This is basically saying \"what if we need more abstraction\", then \"we simply abstract more!\"","updated":"2025-01-09T00:45:16.641Z","document":{"title":"Assembly Language for x86 Processors (Sixth edition)","link":[{"href":"urn:x-pdf:72d08f931fa25ac84e2dfc8557061efb"},{"href":"vault:/book notes/book pdfs /cs271 6th edition version.pdf"}],"documentFingerprint":"72d08f931fa25ac84e2dfc8557061efb"},"uri":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","target":[{"source":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","selector":[{"type":"TextPositionSelector","start":58034,"end":58248},{"type":"TextQuoteSelector","exact":"Then another virtual machine, VM2, can bedesigned  that  is  more  easily  understood.  This  process  can  be  repeated  until  a  virtual machineVM n  can be designed to support a powerful, easy-to-use language. ","prefix":"e used for useful applications? ","suffix":"The Java programming language is"}]}]}
>```
>%%
>*%%PREFIX%%e used for useful applications?%%HIGHLIGHT%% ==Then another virtual machine, VM2, can bedesigned  that  is  more  easily  understood.  This  process  can  be  repeated  until  a  virtual machineVM n  can be designed to support a powerful, easy-to-use language.== %%POSTFIX%%The Java programming language is*
>%%LINK%%[[#^ahw23mp7lec|show annotation]]
>%%COMMENT%%
>This is basically saying "what if we need more abstraction", then "we simply abstract more!"
>%%TAGS%%
>
^ahw23mp7lec


>%%
>```annotation-json
>{"created":"2025-01-09T00:46:38.590Z","updated":"2025-01-09T00:46:38.590Z","document":{"title":"Assembly Language for x86 Processors (Sixth edition)","link":[{"href":"urn:x-pdf:72d08f931fa25ac84e2dfc8557061efb"},{"href":"vault:/book notes/book pdfs /cs271 6th edition version.pdf"}],"documentFingerprint":"72d08f931fa25ac84e2dfc8557061efb"},"uri":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","target":[{"source":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","selector":[{"type":"TextPositionSelector","start":59068,"end":59078},{"type":"TextQuoteSelector","exact":"Figure 1–1","prefix":" values called machine language.","suffix":" Virtual Machine Levels.Instruct"}]}]}
>```
>%%
>*%%PREFIX%%values called machine language.%%HIGHLIGHT%% ==Figure 1–1== %%POSTFIX%%Virtual Machine Levels.Instruct*
>%%LINK%%[[#^ivmyj3gso6|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^ivmyj3gso6


>%%
>```annotation-json
>{"created":"2025-01-09T00:50:02.343Z","text":"explanation on bit orientations. \n","updated":"2025-01-09T00:50:02.343Z","document":{"title":"Assembly Language for x86 Processors (Sixth edition)","link":[{"href":"urn:x-pdf:72d08f931fa25ac84e2dfc8557061efb"},{"href":"vault:/book notes/book pdfs /cs271 6th edition version.pdf"}],"documentFingerprint":"72d08f931fa25ac84e2dfc8557061efb"},"uri":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","target":[{"source":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","selector":[{"type":"TextPositionSelector","start":63033,"end":63140},{"type":"TextQuoteSelector","exact":"left is called the most significant bit (MSB), and the bit on the right is the least significant bit (LSB).","prefix":"e10 Chapter 1  •  Basic Concepts","suffix":"The MSB and LSB bit numbers of a"}]}]}
>```
>%%
>*%%PREFIX%%e10 Chapter 1  •  Basic Concepts%%HIGHLIGHT%% ==left is called the most significant bit (MSB), and the bit on the right is the least significant bit (LSB).== %%POSTFIX%%The MSB and LSB bit numbers of a*
>%%LINK%%[[#^87cyfvaxip5|show annotation]]
>%%COMMENT%%
>explanation on bit orientations. 
>
>%%TAGS%%
>
^87cyfvaxip5


>%%
>```annotation-json
>{"created":"2025-01-09T00:54:05.734Z","text":"If I can remember anything at all, I hope I can remember this. ","updated":"2025-01-09T00:54:05.734Z","document":{"title":"Assembly Language for x86 Processors (Sixth edition)","link":[{"href":"urn:x-pdf:72d08f931fa25ac84e2dfc8557061efb"},{"href":"vault:/book notes/book pdfs /cs271 6th edition version.pdf"}],"documentFingerprint":"72d08f931fa25ac84e2dfc8557061efb"},"uri":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","target":[{"source":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","selector":[{"type":"TextPositionSelector","start":67160,"end":67345},{"type":"TextQuoteSelector","exact":"The  basic  storage  unit  for  all  data  in  an  x86  computer  is  a  byte,  containing  8  bits.  Otherstorage sizes are word (2 bytes), doubleword (4 bytes), and quadword (8 bytes)","prefix":"alue.1.3.3 Integer Storage Sizes","suffix":". In the followingfigure, the nu"}]}]}
>```
>%%
>*%%PREFIX%%alue.1.3.3 Integer Storage Sizes%%HIGHLIGHT%% ==The  basic  storage  unit  for  all  data  in  an  x86  computer  is  a  byte,  containing  8  bits.  Otherstorage sizes are word (2 bytes), doubleword (4 bytes), and quadword (8 bytes)== %%POSTFIX%%. In the followingfigure, the nu*
>%%LINK%%[[#^j2hiawmumb|show annotation]]
>%%COMMENT%%
>If I can remember anything at all, I hope I can remember this. 
>%%TAGS%%
>
^j2hiawmumb


>%%
>```annotation-json
>{"created":"2025-01-09T05:14:09.216Z","text":"Good reminder for memory conversions. ","updated":"2025-01-09T05:14:09.216Z","document":{"title":"Assembly Language for x86 Processors (Sixth edition)","link":[{"href":"urn:x-pdf:72d08f931fa25ac84e2dfc8557061efb"},{"href":"vault:/book notes/book pdfs /cs271 6th edition version.pdf"}],"documentFingerprint":"72d08f931fa25ac84e2dfc8557061efb"},"uri":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","target":[{"source":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","selector":[{"type":"TextPositionSelector","start":67493,"end":67606},{"type":"TextQuoteSelector","exact":"Large Measurements A  number  of  large  measurements  are  used  when  referring  to  bothmemory and disk space:","prefix":" each type of unsigned integer. ","suffix":"• One kilobyte is equal to 210, "}]}]}
>```
>%%
>*%%PREFIX%%each type of unsigned integer.%%HIGHLIGHT%% ==Large Measurements A  number  of  large  measurements  are  used  when  referring  to  bothmemory and disk space:== %%POSTFIX%%• One kilobyte is equal to 210,*
>%%LINK%%[[#^ixu4vqzfi6p|show annotation]]
>%%COMMENT%%
>Good reminder for memory conversions. 
>%%TAGS%%
>
^ixu4vqzfi6p


>%%
>```annotation-json
>{"created":"2025-01-09T18:17:15.711Z","text":"Important note on the way addresses work depending on the mode a program is running in. ","updated":"2025-01-09T18:17:15.711Z","document":{"title":"Assembly Language for x86 Processors (Sixth edition)","link":[{"href":"urn:x-pdf:72d08f931fa25ac84e2dfc8557061efb"},{"href":"vault:/book notes/book pdfs /cs271 6th edition version.pdf"}],"documentFingerprint":"72d08f931fa25ac84e2dfc8557061efb"},"uri":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","target":[{"source":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","selector":[{"type":"TextPositionSelector","start":130523,"end":130770},{"type":"TextQuoteSelector","exact":"In real-address mode, only 1 MByte of memory can be addressed, from hexadecimal 00000to FFFFF. The processor can run only one program at a time, but it can momentarily interruptthat program to process requests (called interrupts) from peripherals.","prefix":"ctly accessing system hardware. ","suffix":" Application programs arepermitt"}]}]}
>```
>%%
>*%%PREFIX%%ctly accessing system hardware.%%HIGHLIGHT%% ==In real-address mode, only 1 MByte of memory can be addressed, from hexadecimal 00000to FFFFF. The processor can run only one program at a time, but it can momentarily interruptthat program to process requests (called interrupts) from peripherals.== %%POSTFIX%%Application programs arepermitt*
>%%LINK%%[[#^xi6l96310if|show annotation]]
>%%COMMENT%%
>Important note on the way addresses work depending on the mode a program is running in. 
>%%TAGS%%
>
^xi6l96310if


>%%
>```annotation-json
>{"created":"2025-01-09T18:18:16.103Z","updated":"2025-01-09T18:18:16.103Z","document":{"title":"Assembly Language for x86 Processors (Sixth edition)","link":[{"href":"urn:x-pdf:72d08f931fa25ac84e2dfc8557061efb"},{"href":"vault:/book notes/book pdfs /cs271 6th edition version.pdf"}],"documentFingerprint":"72d08f931fa25ac84e2dfc8557061efb"},"uri":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","target":[{"source":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","selector":[{"type":"TextPositionSelector","start":131007,"end":131022},{"type":"TextQuoteSelector","exact":" protected mode","prefix":"8can be booted into this mode.In","suffix":", the processor can run multiple"}]}]}
>```
>%%
>*%%PREFIX%%8can be booted into this mode.In%%HIGHLIGHT%% ==protected mode== %%POSTFIX%%, the processor can run multiple*
>%%LINK%%[[#^ovl6oscnbe9|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^ovl6oscnbe9


>%%
>```annotation-json
>{"created":"2025-01-09T18:32:46.204Z","text":"refresher on mth 231 syntax ","updated":"2025-01-09T18:32:46.204Z","document":{"title":"Assembly Language for x86 Processors (Sixth edition)","link":[{"href":"urn:x-pdf:72d08f931fa25ac84e2dfc8557061efb"},{"href":"vault:/book notes/book pdfs /cs271 6th edition version.pdf"}],"documentFingerprint":"72d08f931fa25ac84e2dfc8557061efb"},"uri":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","target":[{"source":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","selector":[{"type":"TextPositionSelector","start":85929,"end":86133},{"type":"TextQuoteSelector","exact":"Boolean Expression A  boolean  expression  involves  a  boolean  operator  and  one  or  moreoperands. Each boolean expression implies a value of true or false. The set of operators includesthe folllowing","prefix":"s to express logical operations.","suffix":":• NOT: notated as ¬ or ~ or ’• "}]}]}
>```
>%%
>*%%PREFIX%%s to express logical operations.%%HIGHLIGHT%% ==Boolean Expression A  boolean  expression  involves  a  boolean  operator  and  one  or  moreoperands. Each boolean expression implies a value of true or false. The set of operators includesthe folllowing== %%POSTFIX%%:• NOT: notated as ¬ or ~ or ’•*
>%%LINK%%[[#^3ac7pvpsmt|show annotation]]
>%%COMMENT%%
>refresher on mth 231 syntax 
>%%TAGS%%
>
^3ac7pvpsmt


>%%
>```annotation-json
>{"created":"2025-01-09T18:34:14.604Z","text":"section about cpu design ","updated":"2025-01-09T18:34:14.604Z","document":{"title":"Assembly Language for x86 Processors (Sixth edition)","link":[{"href":"urn:x-pdf:72d08f931fa25ac84e2dfc8557061efb"},{"href":"vault:/book notes/book pdfs /cs271 6th edition version.pdf"}],"documentFingerprint":"72d08f931fa25ac84e2dfc8557061efb"},"uri":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","target":[{"source":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","selector":[{"type":"TextPositionSelector","start":97332,"end":97566},{"type":"TextQuoteSelector","exact":"The   central  processorunit  (CPU), where calculations and logic operations take place, contains a limited number ofstorage  locations  named   registers ,  a  high-frequency  clock,  a  control  unit,  and  an  arithmeticlogic unit.","prefix":"  hypothetical  microcomputer.  ","suffix":" • The  clock  synchronizes the "}]}]}
>```
>%%
>*%%PREFIX%%hypothetical  microcomputer.%%HIGHLIGHT%% ==The   central  processorunit  (CPU), where calculations and logic operations take place, contains a limited number ofstorage  locations  named   registers ,  a  high-frequency  clock,  a  control  unit,  and  an  arithmeticlogic unit.== %%POSTFIX%%• The  clock  synchronizes the*
>%%LINK%%[[#^xi8hir491to|show annotation]]
>%%COMMENT%%
>section about cpu design 
>%%TAGS%%
>
^xi8hir491to


>%%
>```annotation-json
>{"created":"2025-01-09T18:36:09.023Z","updated":"2025-01-09T18:36:09.023Z","document":{"title":"Assembly Language for x86 Processors (Sixth edition)","link":[{"href":"urn:x-pdf:72d08f931fa25ac84e2dfc8557061efb"},{"href":"vault:/book notes/book pdfs /cs271 6th edition version.pdf"}],"documentFingerprint":"72d08f931fa25ac84e2dfc8557061efb"},"uri":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","target":[{"source":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","selector":[{"type":"TextPositionSelector","start":98632,"end":98729},{"type":"TextQuoteSelector","exact":"A  bus  is a group of parallel wires that transfer data from one part of the computer to another.","prefix":"ructions can be copied together.","suffix":"A computer system usually contai"}]}]}
>```
>%%
>*%%PREFIX%%ructions can be copied together.%%HIGHLIGHT%% ==A  bus  is a group of parallel wires that transfer data from one part of the computer to another.== %%POSTFIX%%A computer system usually contai*
>%%LINK%%[[#^5yjgepoithr|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^5yjgepoithr


>%%
>```annotation-json
>{"created":"2025-01-09T18:37:11.326Z","updated":"2025-01-09T18:37:11.326Z","document":{"title":"Assembly Language for x86 Processors (Sixth edition)","link":[{"href":"urn:x-pdf:72d08f931fa25ac84e2dfc8557061efb"},{"href":"vault:/book notes/book pdfs /cs271 6th edition version.pdf"}],"documentFingerprint":"72d08f931fa25ac84e2dfc8557061efb"},"uri":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","target":[{"source":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","selector":[{"type":"TextPositionSelector","start":100614,"end":100790},{"type":"TextQuoteSelector","exact":" Instructions requiringmemory access often have empty clock cycles called  wait states  because of the differences in thespeeds of the CPU, the system bus, and memory circuits.","prefix":"he 8088 processor, for example).","suffix":" 2.1.2 Instruction Execution Cyc"}]}]}
>```
>%%
>*%%PREFIX%%he 8088 processor, for example).%%HIGHLIGHT%% ==Instructions requiringmemory access often have empty clock cycles called  wait states  because of the differences in thespeeds of the CPU, the system bus, and memory circuits.== %%POSTFIX%%2.1.2 Instruction Execution Cyc*
>%%LINK%%[[#^7we19v4scgp|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^7we19v4scgp



>%%
>```annotation-json
>{"created":"2025-01-09T18:40:57.531Z","text":"important note on the step by step that goes into executing instructions. ","updated":"2025-01-09T18:40:57.531Z","document":{"title":"Assembly Language for x86 Processors (Sixth edition)","link":[{"href":"urn:x-pdf:72d08f931fa25ac84e2dfc8557061efb"},{"href":"vault:/book notes/book pdfs /cs271 6th edition version.pdf"}],"documentFingerprint":"72d08f931fa25ac84e2dfc8557061efb"},"uri":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","target":[{"source":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","selector":[{"type":"TextPositionSelector","start":101178,"end":101431},{"type":"TextQuoteSelector","exact":"Executing  a  machine  instruction  requiresthree basic steps:  fetch,   decode,  and  execute.  Two more steps are required when the instructionuses a memory operand:  fetch operand  and  store output operand . Each of the steps is describedas follows:","prefix":"ions  about  to  be  executed.  ","suffix":" • Fetch:  The control unit fetc"}]}]}
>```
>%%
>*%%PREFIX%%ions  about  to  be  executed.%%HIGHLIGHT%% ==Executing  a  machine  instruction  requiresthree basic steps:  fetch,   decode,  and  execute.  Two more steps are required when the instructionuses a memory operand:  fetch operand  and  store output operand . Each of the steps is describedas follows:== %%POSTFIX%%• Fetch:  The control unit fetc*
>%%LINK%%[[#^othhjj2b0uc|show annotation]]
>%%COMMENT%%
>important note on the step by step that goes into executing instructions. 
>%%TAGS%%
>
^othhjj2b0uc


>%%
>```annotation-json
>{"created":"2025-01-09T18:53:22.961Z","updated":"2025-01-09T18:53:22.961Z","document":{"title":"Assembly Language for x86 Processors (Sixth edition)","link":[{"href":"urn:x-pdf:72d08f931fa25ac84e2dfc8557061efb"},{"href":"vault:/book notes/book pdfs /cs271 6th edition version.pdf"}],"documentFingerprint":"72d08f931fa25ac84e2dfc8557061efb"},"uri":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","target":[{"source":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","selector":[{"type":"TextPositionSelector","start":106068,"end":106084},{"type":"TextQuoteSelector","exact":"How Programs Run","prefix":" when the cache is large. 2.1.4 ","suffix":" Load and Execute Process The fo"}]}]}
>```
>%%
>*%%PREFIX%%when the cache is large. 2.1.4%%HIGHLIGHT%% ==How Programs Run== %%POSTFIX%%Load and Execute Process The fo*
>%%LINK%%[[#^tyabrdxd7v|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^tyabrdxd7v


>%%
>```annotation-json
>{"created":"2025-01-09T18:56:13.326Z","updated":"2025-01-09T18:56:13.326Z","document":{"title":"Assembly Language for x86 Processors (Sixth edition)","link":[{"href":"urn:x-pdf:72d08f931fa25ac84e2dfc8557061efb"},{"href":"vault:/book notes/book pdfs /cs271 6th edition version.pdf"}],"documentFingerprint":"72d08f931fa25ac84e2dfc8557061efb"},"uri":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","target":[{"source":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","selector":[{"type":"TextPositionSelector","start":109988,"end":110334},{"type":"TextQuoteSelector","exact":"A  multitasking  OS  runs  on  a  processor  (such  as  the  x86)  that  supports   task  switching. The processor saves the state of each task before switching to a new one. A task’s  state  consistsof  the  contents  of  the  processor  registers,  program  counter,  and  status  flags,  along  with  refer-ences to the task’s memory segments.","prefix":"gure 2–4 Round-Robin Scheduler. ","suffix":" A multitasking OS will usually "}]}]}
>```
>%%
>*%%PREFIX%%gure 2–4 Round-Robin Scheduler.%%HIGHLIGHT%% ==A  multitasking  OS  runs  on  a  processor  (such  as  the  x86)  that  supports   task  switching. The processor saves the state of each task before switching to a new one. A task’s  state  consistsof  the  contents  of  the  processor  registers,  program  counter,  and  status  flags,  along  with  refer-ences to the task’s memory segments.== %%POSTFIX%%A multitasking OS will usually*
>%%LINK%%[[#^19sqy3h2yk1j|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^19sqy3h2yk1j


>%%
>```annotation-json
>{"created":"2025-01-09T18:57:01.516Z","updated":"2025-01-09T18:57:01.516Z","document":{"title":"Assembly Language for x86 Processors (Sixth edition)","link":[{"href":"urn:x-pdf:72d08f931fa25ac84e2dfc8557061efb"},{"href":"vault:/book notes/book pdfs /cs271 6th edition version.pdf"}],"documentFingerprint":"72d08f931fa25ac84e2dfc8557061efb"},"uri":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","target":[{"source":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","selector":[{"type":"TextPositionSelector","start":112159,"end":112356},{"type":"TextQuoteSelector","exact":"x86 processors have three primary modes of operation: protected mode, real-address mode, andsystem  management  mode.  A  sub-mode,  named   virtual-8086 ,  is  a  special  case  of  protectedmode.","prefix":"sors.  2.2.1 Modes of Operation ","suffix":" Here are short descriptions of "}]}]}
>```
>%%
>*%%PREFIX%%sors.  2.2.1 Modes of Operation%%HIGHLIGHT%% ==x86 processors have three primary modes of operation: protected mode, real-address mode, andsystem  management  mode.  A  sub-mode,  named   virtual-8086 ,  is  a  special  case  of  protectedmode.== %%POSTFIX%%Here are short descriptions of*
>%%LINK%%[[#^9c6uqrvrbtb|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^9c6uqrvrbtb


>%%
>```annotation-json
>{"created":"2025-01-09T18:59:04.168Z","text":"refresher on what the registers mean","updated":"2025-01-09T18:59:04.168Z","document":{"title":"Assembly Language for x86 Processors (Sixth edition)","link":[{"href":"urn:x-pdf:72d08f931fa25ac84e2dfc8557061efb"},{"href":"vault:/book notes/book pdfs /cs271 6th edition version.pdf"}],"documentFingerprint":"72d08f931fa25ac84e2dfc8557061efb"},"uri":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","target":[{"source":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","selector":[{"type":"TextPositionSelector","start":114755,"end":114896},{"type":"TextQuoteSelector","exact":"There are eight general-purpose registers, six segment registers, aprocessor status flags register (EFLAGS), and an instruction pointer (EIP)","prefix":"sicprogram execution registers. ","suffix":".Figure 2–5 Basic Program Execut"}]}]}
>```
>%%
>*%%PREFIX%%sicprogram execution registers.%%HIGHLIGHT%% ==There are eight general-purpose registers, six segment registers, aprocessor status flags register (EFLAGS), and an instruction pointer (EIP)== %%POSTFIX%%.Figure 2–5 Basic Program Execut*
>%%LINK%%[[#^8gxypwxpn8|show annotation]]
>%%COMMENT%%
>refresher on what the registers mean
>%%TAGS%%
>
^8gxypwxpn8


>%%
>```annotation-json
>{"created":"2025-01-09T19:00:30.595Z","text":"really good information on the different purposes some registers use. ","updated":"2025-01-09T19:00:30.595Z","document":{"title":"Assembly Language for x86 Processors (Sixth edition)","link":[{"href":"urn:x-pdf:72d08f931fa25ac84e2dfc8557061efb"},{"href":"vault:/book notes/book pdfs /cs271 6th edition version.pdf"}],"documentFingerprint":"72d08f931fa25ac84e2dfc8557061efb"},"uri":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","target":[{"source":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","selector":[{"type":"TextPositionSelector","start":115735,"end":115804},{"type":"TextQuoteSelector","exact":"Specialized Uses Some general-purpose registers have specialized uses","prefix":"as shown in the following table:","suffix":":• EAX is automatically used by "}]}]}
>```
>%%
>*%%PREFIX%%as shown in the following table:%%HIGHLIGHT%% ==Specialized Uses Some general-purpose registers have specialized uses== %%POSTFIX%%:• EAX is automatically used by*
>%%LINK%%[[#^4ke9ixua35v|show annotation]]
>%%COMMENT%%
>really good information on the different purposes some registers use. 
>%%TAGS%%
>
^4ke9ixua35v


>%%
>```annotation-json
>{"created":"2025-01-09T19:34:40.909Z","text":"a ctf player's favorite register ","updated":"2025-01-09T19:34:40.909Z","document":{"title":"Assembly Language for x86 Processors (Sixth edition)","link":[{"href":"urn:x-pdf:72d08f931fa25ac84e2dfc8557061efb"},{"href":"vault:/book notes/book pdfs /cs271 6th edition version.pdf"}],"documentFingerprint":"72d08f931fa25ac84e2dfc8557061efb"},"uri":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","target":[{"source":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","selector":[{"type":"TextPositionSelector","start":115983,"end":116158},{"type":"TextQuoteSelector","exact":"ESP addresses data on the stack (a system memory structure). It is rarely used for ordinaryarithmetic or data transfer. It is often called the extended stack pointer register.","prefix":"ly uses ECX as a loop counter.• ","suffix":"• ESI and EDI are used by high-s"}]}]}
>```
>%%
>*%%PREFIX%%ly uses ECX as a loop counter.•%%HIGHLIGHT%% ==ESP addresses data on the stack (a system memory structure). It is rarely used for ordinaryarithmetic or data transfer. It is often called the extended stack pointer register.== %%POSTFIX%%• ESI and EDI are used by high-s*
>%%LINK%%[[#^xnk8b3xf0hb|show annotation]]
>%%COMMENT%%
>a ctf player's favorite register 
>%%TAGS%%
>
^xnk8b3xf0hb


>%%
>```annotation-json
>{"created":"2025-01-09T19:35:05.707Z","text":"my personal fav register","updated":"2025-01-09T19:35:05.707Z","document":{"title":"Assembly Language for x86 Processors (Sixth edition)","link":[{"href":"urn:x-pdf:72d08f931fa25ac84e2dfc8557061efb"},{"href":"vault:/book notes/book pdfs /cs271 6th edition version.pdf"}],"documentFingerprint":"72d08f931fa25ac84e2dfc8557061efb"},"uri":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","target":[{"source":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","selector":[{"type":"TextPositionSelector","start":116319,"end":116581},{"type":"TextQuoteSelector","exact":"EBP is used by high-level languages to reference function parameters and local variables onthe stack. It should not be used for ordinary arithmetic or data transfer except at an advancedlevel of programming. It is often called the extended frame pointer register","prefix":"d destination index registers.• ","suffix":".Segment Registers In real-addre"}]}]}
>```
>%%
>*%%PREFIX%%d destination index registers.•%%HIGHLIGHT%% ==EBP is used by high-level languages to reference function parameters and local variables onthe stack. It should not be used for ordinary arithmetic or data transfer except at an advancedlevel of programming. It is often called the extended frame pointer register== %%POSTFIX%%.Segment Registers In real-addre*
>%%LINK%%[[#^u5wug9w3s7|show annotation]]
>%%COMMENT%%
>my personal fav register
>%%TAGS%%
>
^u5wug9w3s7


>%%
>```annotation-json
>{"created":"2025-01-09T21:54:37.789Z","text":"this is probably talking about stack frames here. ","updated":"2025-01-09T21:54:37.789Z","document":{"title":"Assembly Language for x86 Processors (Sixth edition)","link":[{"href":"urn:x-pdf:72d08f931fa25ac84e2dfc8557061efb"},{"href":"vault:/book notes/book pdfs /cs271 6th edition version.pdf"}],"documentFingerprint":"72d08f931fa25ac84e2dfc8557061efb"},"uri":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","target":[{"source":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","selector":[{"type":"TextPositionSelector","start":116910,"end":116984},{"type":"TextQuoteSelector","exact":"stack  segment  holds  local  function  variables  andfunction parameters.","prefix":"  another  segment  named  the  ","suffix":" Instruction Pointer The  EIP,  "}]}]}
>```
>%%
>*%%PREFIX%%another  segment  named  the%%HIGHLIGHT%% ==stack  segment  holds  local  function  variables  andfunction parameters.== %%POSTFIX%%Instruction Pointer The  EIP,*
>%%LINK%%[[#^46cqm8jd96q|show annotation]]
>%%COMMENT%%
>this is probably talking about stack frames here. 
>%%TAGS%%
>
^46cqm8jd96q


>%%
>```annotation-json
>{"created":"2025-01-09T22:00:33.560Z","text":"don't think these will pop in terms of coding, but they are something to take a note of  ","updated":"2025-01-09T22:00:33.560Z","document":{"title":"Assembly Language for x86 Processors (Sixth edition)","link":[{"href":"urn:x-pdf:72d08f931fa25ac84e2dfc8557061efb"},{"href":"vault:/book notes/book pdfs /cs271 6th edition version.pdf"}],"documentFingerprint":"72d08f931fa25ac84e2dfc8557061efb"},"uri":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","target":[{"source":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","selector":[{"type":"TextPositionSelector","start":118102,"end":118114},{"type":"TextQuoteSelector","exact":"Status Flags","prefix":" Direction and Interrupt flags. ","suffix":" The  Status  flags  reflect  th"}]}]}
>```
>%%
>*%%PREFIX%%Direction and Interrupt flags.%%HIGHLIGHT%% ==Status Flags== %%POSTFIX%%The  Status  flags  reflect  th*
>%%LINK%%[[#^whnhjip4k|show annotation]]
>%%COMMENT%%
>don't think these will pop in terms of coding, but they are something to take a note of  
>%%TAGS%%
>
^whnhjip4k


>%%
>```annotation-json
>{"created":"2025-01-09T22:32:20.532Z","text":"extra program mode specifically for 64 bit systems that allow for 32 bit compatability. ","updated":"2025-01-09T22:32:20.532Z","document":{"title":"Assembly Language for x86 Processors (Sixth edition)","link":[{"href":"urn:x-pdf:72d08f931fa25ac84e2dfc8557061efb"},{"href":"vault:/book notes/book pdfs /cs271 6th edition version.pdf"}],"documentFingerprint":"72d08f931fa25ac84e2dfc8557061efb"},"uri":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","target":[{"source":"vault:/book notes/book pdfs /cs271 6th edition version.pdf","selector":[{"type":"TextPositionSelector","start":124592,"end":124603},{"type":"TextQuoteSelector","exact":"IA-32e Mode","prefix":"  designedfor 64-bit processing.","suffix":" IA-32e Mode has two sub-modes, "}]}]}
>```
>%%
>*%%PREFIX%%designedfor 64-bit processing.%%HIGHLIGHT%% ==IA-32e Mode== %%POSTFIX%%IA-32e Mode has two sub-modes,*
>%%LINK%%[[#^ez6k4eib11w|show annotation]]
>%%COMMENT%%
>extra program mode specifically for 64 bit systems that allow for 32 bit compatability. 
>%%TAGS%%
>
^ez6k4eib11w
