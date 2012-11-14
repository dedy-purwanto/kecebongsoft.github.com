Title: owler.io inbox
Tags: owler.io

I launched owler.io a day before PyCon Apac 2012 has started, it was all
a rush. I'm trying my best to make it work before the conference started
for one single reason: show it at the lighting talk.

You can probably guess how this could affect the internal system: some
hacks, unstructured stuff that is painful to see. But not only that,
also there are untested stuff that make me ashamed of my self. Owler.io
was kind of a suprise project, there were no planning, the idea just
came across and I just sort of did it, no long-term vision and all. This
makes the codebase has no solid grounds, it was all came from guessing.
I have quite experiences in the web side, but on the email service side,
almost zero. I came across Kenneth's inbox.py and just blindly implements
everything in my head.

But having things working, although messy, thaught me a lot of things,
especially what the system really need, and how it should handle things.

Since I'm planning to make this thing open to everyone, I think it's okay
if I put whatever's in my head about how things should work in here as
well.

In case if some of you don't know, owler.io is simple a service that 
let's you create bitbucket or github issue by sending email to 
*[your_repository_name]@owler.io. It's that simple. There are two main
things in owler.io: A web interface that let's you register and manage
your repository and other information, and an inbox daemon that listen
to all incoming mails and process them accordingly.

As I stated before, the web interface isn't the trickiest since it all
just a simple data management and I had quite an experience with Django.
The email service, in the other hand, was quite new and although it
was simple to implement the starting grid of it, most of the feature
and safety rules aren't there. Things went fine at the launch day,
until few weeks later when I create some use from my gmail, the email
service received multiple same email and it created multiple same issues
in the repository, and it was my company's repository!.

I started to realize that this thing could go even worse, for example,
there are no email spoofing handling, and that itself was quite a
complex issue to tackle, there are exact way to prevent this from 
happening. Lucky this bug occured to me before anybody else get it. I
realize that I need to shut it down temporarely and make it significantly
more secure while still make it convenient to use.

There are things in my mind on how to tackle this two problem. Avoiding
multiple creation on the same issue might be solved by creating a 
signature or a checksum on each incoming email. The other problem,
which is email spoofing, cannot be solved easily. The most possible way
to make sure no hacker can create issue by spoofing email address is
by sending a confirmation link to the sender, and ask them to click
the link to confirm and create the issue. 

This will affect the user experience of using the service, and it will
also rise a problem of spamming the original sender. But I realize that
this is the most possible way to implement because it's dead simple,
it's safer, and trying to be write my own handler to prevent spoofing
might not be unpleasant to anyone.
