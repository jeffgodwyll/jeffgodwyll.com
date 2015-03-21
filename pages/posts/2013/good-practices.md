title: Good C++ Practices
date: 2013-05-22
published: true

<!-- tags: [Code] -->

"Refactored" or “forked” from http://www.cplusplus.com/forum/lounge/6195/  
  
You might want to check the original out or just go by these “commandments” and write better C++ code in general. These good practices will in one way or the other save you some headache like the ones I get at times 
  
1\. Always use header guards.  
  
2\. Always follow The Standard.  
> Never include any header that's not one of these:
>
> - A standard header, 
> - A header of a library you're using or 
> - A system API header. 
>
> Never include compiler-specific headers. Compilers come and go, but the language and the systems stay."  
  
3\. Do not `#include` cpp files in other cpp files (Especially when using IDEs).  
> It's generally a better idea to use headers to declare class and function names, as multiple declarations don't cause the compiler to raise errors, while multiple definitions do.  
  
4\. Use indentation.  
> For example, I indent using tab spaces(soft tabs) or 4 spaces inside each block.  
  
5\. Adopt a naming convention and be consistent.  
> There are a whole bunch of advices out there for newbies but I feel the real advice should be: adopt a naming style and try to keep the naming consistent and meaningful especially when you are not the only one going to work with it. Remember not to touch reserved words. That’s about it.  
  
6\. Use whitespace.  
> You know, for clarity! This is a no brainer really. Who wouldn’t use whitespace? Even text editors (except the crappy ones of course) and IDE’s include them whether you like it or YES ;p  
  
7\. "Functionize!"  
> Inheritance becomes a breeze + makes everything simpler. The reason I love java atm.  
  
8\. Use `const` correctly.  
  
9\. Include exceptions to handle runtime errors.  
> You probably don’t want your program to hang during runtime so just include them and be free. Oh and always ignore that little voice that likes to start sentences like "why would anyone want to..." and "what kind of “mental nerd” would try to...”. Unless you the programmer is also the user or the only user, there's always someone who wants to do it, and a “mental nerd” who tries to do it. It's advisable to obey users and punish “mental nerds”. Oh and finally you the programmer, please try to think like a “mental nerd” would. It helps in dealing with them in general.  
  
10\. Ask for help and advice.  
> I believe this to be the best along with the next. Try to analyze what you've put down for what it actually does and not what you expect it to do. Beginners (and not so beginners) all too often either fall into the habit of either asking for help the instant something isn't obvious, or spend days trying to solve a minor problem before asking for help. Remember the 30-minute-rule, [google](https://google.com) it or head over to [stackoverflow](https://stackoverflow.com).  
  
11\. Take a break.  
> There’s the tendency to spend hours on end coding or figuring out what something does. It can be fun (like seriously). Just don't be afraid to stop and walk away for a few when something is kicking your butt. If you stay, your frustration grows and the answer gets further from your mind (at least it does for me). Be sure to keep a video game in or nearby the system where you do your coding so that can relax you during these periods. Something not too exciting is preferable (Although I delight in beating someone to an "exciting" game or 2 of FIFA). It's also probably better if you don't need to think too much to play it. 

Additionlly, when looking through code for errors, it's sometimes useful to go backwards. That way you look at each line for what it is rather than what you expect it to be.
