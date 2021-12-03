# evil_bit.py
A tool for RFC-3514 compliant pentesting

# Motivation
On April 1st, 2003, Steven M. Bellovin released RFC-3514 via the Networking Group of the IETF.
In that RFC, he made a simple, yet ground-breaking recommendation: designate the heretofore unused high-bit within the IP packet's "flags" field to designate whether a packet's contents had evil intent. Now, what was once known as the "reserved bit" became the "evil bit."

This presented a boon for those of us charged with protecting networks. 

* Firewalls could be simplified
    * No need for deep packet inspection
    * No need for "next generation"
    * Simply looking at a single bit was all that was necessary to decide if a packet should be blocked.

* Two months after the release of RFC-3514, in June of 2003, Gartner declared the IDS "dead."
    * Coincidence?
    * I think not!

* A new age of secure networks was about to dawn!

# Reality comes crashing down...

Unfortunately, bad actors on the Internet were somewhat reluctant to adopt and comply with RFC-3514.

Why? 

I think that the explanation is simple: the security community set a bad example.

We spend our days performing pentests and throwing all kinds of evil traffic at networks, but do WE comply with RFC-3514?

NO!

# Filling a void

*Why do you look at the speck of sawdust in your brother’s eye and pay no attention to the plank in your own eye? How can you say to your brother, "Let me take the speck out of your eye," when all the time there is a plank in your own eye? You hypocrite, first take the plank out of your own eye, and then you will see clearly to remove the speck from your brother’s eye.* **- Matthew 7:3-5 NIV**

We're hypocrites. No doubt about it. But I'm here to help. 

Run this little python script as root.

# Prerequisites

```sudo apt install python3-pip python3-scapy git libnfnetlink-dev libnetfilter-queue-dev```

as root:

```pip3 install -U git+https://github.com/kti/python-netfilterqueue```

then:

```sudo iptables -A OUTPUT -o <device> -p IP -j NFQUEUE --queue-num 3514```

replacing <device\> with the correct device name.

# Finally

Bask in your RFC-3514 compliance...

# And now for something completely different...

If, perchance, you're one of those antisocial people who isn't interested in setting a good example by being RFC compliant, you might find this an interesting example of how you can use iptables' netfilter queues combined with scapy to rewrite packet contents on the fly, correcting checksums where necessary, all within the comfort of Python. You might find that useful for other things as well

Who knows?