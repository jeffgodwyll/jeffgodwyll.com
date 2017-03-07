title: Dotfile Goodness, Vim!
date: 2016-11-21
published: true

This post focuses on Vim and is a part of a series of posts describing my
development environment: zsh, Vim, tmux, etc.

![][vim_img]

This is my primary motivation for this post:

![][why_this_post]

So let's get started

### ⇛ Installing Vim (optional)

Chances are you already have Vim on your system if you're on a Unix or Unix-like
system.

On a Mac, you can get the most recent version of Vim with [Homebrew][homebrew],
the one and only package manager :p.

    $ brew install vim

Ubuntu:

    $ sudo apt-get install vim


### ⇛ Vim Modes

People in the Vi(m) community do not really agree on how many modes there are,
but hey let me add to the <del>confusion</del>/debate.

The main things you'll find yourself doing include:

 - entering some sort of command or key combos which manipulate text, files...
 - actually entering text, that's what a text editor should do right

With that out of the way, there's the:

#### Normal Mode
This is the default mode you'll find yourself in, each time you're in Vim. In
this mode you can navigate your way through text with <kbd>h</kbd><kbd>j</kbd>
<kbd>k</kbd><kbd>l</kbd>. These conveniently happen to be home row keys as well.

 - <kbd>h</kbd> moves one character to the left.
 - <kbd>j</kbd> moves down a line.
 - <kbd>k</kbd> moves up a line.
 - <kbd>l</kbd> moves one character to the right.

The following keys make movement simpler as well

- <kbd>0</kbd> moves the cursor to the beginning of the line.
- <kbd>$</kbd> moves the cursor to the end of the line.
- <kbd>w</kbd> move forward one word.
- <kbd>b</kbd> move backward one word.
- <kbd>G</kbd> move to the end of the file.
- <kbd>H</kbd> move to the top of the screen
- <kbd>M</kbd> move to the middle the screen
- <kbd>L</kbd> move to the bottom of the screen
- <kbd>g</kbd><kbd>g</kbd> move to the beginning of the file.
- <kbd>`</kbd><kbd>.</kbd> move to the last edit.

`
It's in this mode that you can perform a number of verbs and modifiers on
nouns(to borrow heavily from [Yan Pritzker's Vim lingo][vim_lingo]).

Then there's the:

#### Insert Mode
This mode allows you to enter text. While you can use commands in a special mode–insert normal
mode(`C-o` i.e <kbd>ctrl</kbd><kbd>o</kbd>), Vim's insert mode is specialized
for one task–entering text.

Enter insert mode with <kbd>i</kbd>

You can use one of the following to get back to normal mode:

- <kbd>esc</kbd>
- <kbd>ctrl</kbd><kbd>[</kbd><span style="font-size:0;">]</span>

#### Visual Mode
In this mode we can define a selection of text and then perform some operations
on the text. This mode is accessible with the <kbd>v</kbd> key, when coming from
the normal mode. There are 3 visual modes though depending on what you're
trying to achieve.

 1. Character-wise,<kbd>v</kbd>
 2. Line-wise, <kbd>V</kbd> i.e (<kbd>⇧</kbd> + <kbd>v</kbd>)
 3. Block-wise,<kbd>ctrl</kbd><kbd>v</kbd>

Hitting <kbd>esc</kbd> will almost always get you back into normal mode.


And finally if you haven't found how to exit Vim yet, you're not alone.

> <blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">I&#39;ve
been using Vim for about 2 years now, mostly because I can&#39;t figure out how
to exit it.</p>&mdash; I Am Devloper (@iamdevloper) <a
href="https://twitter.com/iamdevloper/status/435555976687923200">February 17,
2014</a></blockquote>

To exit vim:

 - <kbd>:</kbd><kbd>q</kbd> to quit
 - <kbd>:</kbd><kbd>w</kbd><kbd>q</kbd> to save changes and quit
 - <kbd>:</kbd><kbd>q</kbd><kbd>!</kbd> to quit discarding changes

### ⇛ Vimtutor
If you're trying out Vim for the first time though, I can't recommend vimtutor
enough. It's by far the quickest way to get familiar with basic key movements,
verbs, etc. etc...

It comes as part of the vim installation process. Just invoke it at the terminal:

    $ vimtutor

### ⇛ General Customizations

I always remap my <kbd>⇪</kbd> into an extra <kbd>esc</kbd> key. I don't use the
caps lock key anyway.

On a Linux system, I do this with [xmodmap][xmodmap].
On a Mac, I achieve something similar with a combination of
[Karabiner][karabiner], formerly known as KeyRemap4MacBook, & [Seil][seil].

### ⇛ My Vim Configuration

In this section I'll attempt at explaining some of the general settings I've set
up in my [vimrc][vimrc]–Vim's config file.

    $ vim ~/.vimrc

Within vim, I also remap <kbd>;</kbd> to <kbd>:</kbd> in normal mode.

    nnoremap ; :

> not using the mouse in vim is so 1970. in the 1980 we also stop moving around
with the arrow keys 😎 beat that!
[Posted in #general Nov 17th at 2:23 PM][yaws_comment]

It helps to just get rid of the mouse. While at it, get rid of the arrow keys as
well. You'll become a pro in moving with the "right" keys in no time at all.

Adding this to your `.vimrc` disables the arrow keys in insert and normal mode

    nnoremap <up> <nop>
    nnoremap <down> <nop>
    nnoremap <left> <nop>
    nnoremap <right> <nop>
    inoremap <up> <nop>
    inoremap <down> <nop>
    inoremap <left> <nop>
    inoremap <right> <nop>

Although I don't agree with the mouse part, it can come in handy:

    set mouse=a

Some sane defaults for searching:

    set hlsearch    " highlight searches "
    set ignorecase  " ignore case "
    set smartcase   " smart search "

With both `ignorecase` and `smartcase` set, if a pattern contains an uppercase
letter, the returned search becomes case sensitive, otherwise it isn't. Comes in
pretty handy.

Show status line:

    set laststatus=2

Show line numbers:

    set number

Show row and column:

    set ruler

Smarter backspacing:

    set backspace=indent,eol,start

I make use of the `<leader>` key as a prefix key for a number of custom key mappings
so as not to mess too much with Vim's defaults. By default this is mapped to
<kbd>\\</kbd>.

It's a good idea to use the `<leader>`, as it's a way of extending the
power of vim shortcuts, in fact many plugins create their own mappings that
start with the `leader`. But <kbd>\\</kbd> is awkward to reach so I remap it.

    let mapleader = ","

That way if you have a map of `<leader>jd`, you can perform that action with
<kbd>,</kbd><kbd>j</kbd><kbd>d</kbd>

#### Plugins FTW!

There are countless Vim plugins lying all over the web. And coming from other
editors, you might start to feel left out. But hey don't fret it. There's always
a plugin for it :)

I use [Vundle][vundle] to manage [my plugins][my_plugs]. It's feature packed
but then allows you to never think about the process of managing plugins ever
once it's set up. Just plug 'em in, even personal plugins.

Installing Vundle:

    $ git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

Once you've added a plugin to your config, you can install it in vim with:

    :PluginInstall

My Vim configuration is heavily geared towards Python Development, but there's
some love thrown in there for JavaScript, CSS, HTML, TypeScript(read: Angular2)
and Markdown. Oh and Java when I'm feeling tipsy at times :D

For appearances, I manage my colours myself, but you can easily use one of the
many colour scheme plugins available. If the terminal is capable of displaying
'colours', all 256 of them, then I load my custom colour scheme:

    if &t_Co >= 256 || has("gui_running")
        color mustang
    endif

And to install a plugin is super simple. Lots of [examples here][my_plugs]

- [vim-airline][], a better status line.

        let g:airline_theme = 'laederon'
        let g:airline_powerline_fonts = 1
        let g:airline#extensions#branch#enabled = 1
        let g:airline#extensions#syntastic#enabled = 1
        let g:airline#extensions#virtualenv#enabled = 1

For File Navigation:

- [ctrlp][], for quick file opening. Sometimes, the only file navigation I need
  really. I use a leader key mapping because the default kinda conflicts with
  some other plugins I've set up ;). It intelligently knows where to look for
  the root of the project you're currently working in. You can extend it too.
  It's just awesome.

        let g:ctrlp_show_hidden = 1
        let g:ctrlp_working_path_mode = 'r'  " r=nearest.git,.hg,.svn,.bzr,_darcs dirs"
        let g:ctrlp_open_new_file = 'v'  " in a new vertical split"

        nmap <leader>p :CtrlP<cr>

- [NERDTree][], for file navigation

        " toggle nerdtree file/folder tree "
        nmap <C-n><C-t> :NERDTreeToggle<CR>


- [tagbar][], for improved code outlines / navigations.


Python specific:

- [jedi-vim][], awesome Python autocompletion with Vim

        let g:jedi#goto_command = '<leader>jd'  " goto definition or assignment
        let g:jedi#goto_assignments_command = '<leader>jg'  " goto assignments
        let g:jedi#rename_command = '<leader>jr' " rename variables

- [vim-jinja][], jinja support.
- [vim-virtualenv][], for Python virtualenv support.
- [python-mode][], static analysis, refactoring, folding, completion, documentation, etc.
- [vim-flake8][], static syntax and style checker for Python.

Autocompletion:

- [YouCompleteMe][ycm], is a fast, as-you-type, fuzzy-search code
  completion engine for Vim.

Snippets:

- [UltiSnips][ultisnips], is the ultimate solution for snippets in Vim.

For git:

- [fugitive][], for git integration, I find it more convenient using git
  directly from the terminal as I have heavily customised my git experience
  there.

Editing markdown documents:

- [vim-livedown][], for live preview of Markdown files
- [Goyo][], distraction-free writing
- [limelight][], hyperfocus-writing in Vim

Other files:

- [syntastic][], syntax checking for various file formats. You can allow Vim to
  check your syntax

- [vim-json][], distinct highlighting of keywords vs values, JSON-specific (non-JS) warnings, quote concealing.
- [MatchTagAlways][], always highlight tag pairs. Makes it easier to find
  closing tags in html-like filetypes.

        let g:mta_filetypes = {
            \ 'html': 1,
            \ 'xhtml': 1,
            \ 'xml': 1,
            \ 'jinja': 1,
            \ 'htmljinja': 1,
            \}

- [emmet-vim][], html code completion.

I've left a couple of the plugins I use out of this post. You'll find them
in [my vim configuration][my_plugs]. But a more exhaustive list of
plugins to install can be found @ vim awesome, linked below in Resources.


### ⇛ Conclusion
It's my hope that at this point, I've helped demystify Vim and that your
experience getting started in Vim is a lot more awesome and painless.


### ⇛ Resources
2. [Practical Vim: Edit Text at the speed of Thought][practical_vim]
3. [Vundle][vundle]
1. [Vim awesome, awesome vim plugins from across the universe][vim_awesome] :)

[vim_img]: https://storage.googleapis.com/jeffgodwyll.appspot.com/dotfile-goodness/vim.png
[why_this_post]: https://storage.googleapis.com/jeffgodwyll.appspot.com/dotfile-goodness/slack.png
[homebrew]: http://brew.sh/
[yaws_comment]: https://devcongress-community.slack.com/archives/general/p1479392600006855
[vim_lingo]: https://yanpritzker.com/learn-to-speak-vim-verbs-nouns-and-modifiers-d7bfed1f6b2d#.lvdazz2rt
[vimrc]: https://github.com/jeffgodwyll/dotfiles/blob/master/.vimrc
[xmodmap]: https://linux.die.net/man/1/xmodmap
[karabiner]: https://pqrs.org/osx/karabiner/
[seil]: https://pqrs.org/osx/karabiner/seil.html.en
[vundle]: https://github.com/VundleVim/Vundle.vim
[vim_awesome]: http://vimawesome.com/
[practical_vim]: https://www.amazon.com/Practical-Vim-Thought-Pragmatic-Programmers/dp/1934356980
[my_plugs]: https://github.com/jeffgodwyll/dotfiles/blob/master/.vimrc#L191

[NERDTree]: https://github.com/scrooloose/nerdtree
[numbers]: https://github.com/myusuf3/numbers.vim.git
[ctrlp]: https://github.com/kien/ctrlp.vim.git
[fugitive]: http://github.com/tpope/vim-fugitive.git
[Goyo]: https://github.com/junegunn/goyo.vim
[vimmarkdown]: https://github.com/tpope/vim-markdown
[vim-livedown]: https://github.com/shime/vim-livedown
[GoldenView]: https://github.com/zhaocai/GoldenView
[syntastic]: https://github.com/scrooloose/syntastic
[jedi-vim]: https://github.com/davidhalter/jedi-vim
[MatchTagAlways]: https://github.com/Valloric/MatchTagAlways
[vim-json]: https://github.com/elzr/vim-json
[vim-jinja2-syntax]: https://github.com/glench/vim-jinja2-syntax
[vim-virtualenv]: https://github.com/jmcantrell/vim-virtualenv
[python-mode]: https://github.com/klen/python-modei
[vim-flake8]: https://github.com/nvie/vim-flake8
[vim-airline]: https://github.com/bling/vim-airline
[emmet-vim]: https://github.com/mattn/emmet-vim
[i3-vim-syntax]: https://github.com/PotatoesMaster/i3-vim-syntax
[limelight]: https://github.com/junegunn/limelight.vim
[tagbar]: https://github.com/majutsushi/tagbar
[vim-powerline]: https://github.com/Lokaltog/vim-powerline
[vim-jinja]: https://github.com/mitsuhiko/vim-jinja
[ycm]: https://github.com/Valloric/YouCompleteMe
[ultisnips]: https://github.com/SirVer/ultisnips
