Code	Meaning
200	(nonstandard success response, see rfc876)
211	System status, or system help reply
214	Help message
220	<domain> Service ready
221	<domain> Service closing transmission channel
250	Requested mail action okay, completed
251	User not local; will forward to <forward-path>
252	Cannot VRFY user, but will accept message and attempt delivery
354	Start mail input; end with <CRLF>.<CRLF>
421	<domain> Service not available, closing transmission channel
450	Requested mail action not taken: mailbox unavailable
451	Requested action aborted: local error in processing
452	Requested action not taken: insufficient system storage
500	Syntax error, command unrecognised
501	Syntax error in parameters or arguments
502	Command not implemented
503	Bad sequence of commands
504	Command parameter not implemented
521	<domain> does not accept mail (see rfc1846)
530	Access denied (???a Sendmailism)
550	Requested action not taken: mailbox unavailable
551	User not local; please try <forward-path>
552	Requested mail action aborted: exceeded storage allocation
553	Requested action not taken: mailbox name not allowed
554	Transaction failed
Reply codes grouped by command
Command	Code	Description
connect
220	<domain> Service ready
421	<domain> Service not available, closing transmission channel
HELO
250	Requested mail action okay, completed
500	Syntax error, command unrecognised
501	Syntax error in parameters or arguments
504	Command parameter not implemented
521	<domain> does not accept mail [rfc1846]
421	<domain> Service not available, closing transmission channel
EHLO
250	Requested mail action okay, completed
550	Not implemented
500	Syntax error, command unrecognised
501	Syntax error in parameters or arguments
504	Command parameter not implemented
421	<domain> Service not available, closing transmission channel
MAIL
250	Requested mail action okay, completed
552	Requested mail action aborted: exceeded storage allocation
451	Requested action aborted: local error in processing
452	Requested action not taken: insufficient system storage
500	Syntax error, command unrecognised
501	Syntax error in parameters or arguments
421	<domain> Service not available, closing transmission channel
RCPT
250	Requested mail action okay, completed
251	User not local; will forward to <forward-path>
550	Requested action not taken: mailbox unavailable
551	User not local; please try <forward-path>
552	Requested mail action aborted: exceeded storage allocation
553	Requested action not taken: mailbox name not allowed
450	Requested mail action not taken: mailbox unavailable
451	Requested action aborted: local error in processing
452	Requested action not taken: insufficient system storage
500	Syntax error, command unrecognised
501	Syntax error in parameters or arguments
503	Bad sequence of commands
521	<domain> does not accept mail [rfc1846]
421	<domain> Service not available, closing transmission channel
DATA
354	Start mail input; end with <CRLF>.<CRLF>
451	Requested action aborted: local error in processing
554	Transaction failed
500	Syntax error, command unrecognised
501	Syntax error in parameters or arguments
503	Bad sequence of commands
421	<domain> Service not available, closing transmission channel
received data
250	Requested mail action okay, completed
552	Requested mail action aborted: exceeded storage allocation
554	Transaction failed
451	Requested action aborted: local error in processing
452	Requested action not taken: insufficient system storage
RSET
200	(nonstandard success response, see rfc876)
250	Requested mail action okay, completed
500	Syntax error, command unrecognised
501	Syntax error in parameters or arguments
504	Command parameter not implemented
421	<domain> Service not available, closing transmission channel
SEND
250	Requested mail action okay, completed
552	Requested mail action aborted: exceeded storage allocation
451	Requested action aborted: local error in processing
452	Requested action not taken: insufficient system storage
500	Syntax error, command unrecognised
501	Syntax error in parameters or arguments
502	Command not implemented
421	<domain> Service not available, closing transmission channel
SOML
250	Requested mail action okay, completed
552	Requested mail action aborted: exceeded storage allocation
451	Requested action aborted: local error in processing
452	Requested action not taken: insufficient system storage
500	Syntax error, command unrecognised
501	Syntax error in parameters or arguments
502	Command not implemented
421	<domain> Service not available, closing transmission channel
SAML
250	Requested mail action okay, completed
552	Requested mail action aborted: exceeded storage allocation
451	Requested action aborted: local error in processing
452	Requested action not taken: insufficient system storage
500	Syntax error, command unrecognised
501	Syntax error in parameters or arguments
502	Command not implemented
421	<domain> Service not available, closing transmission channel
VRFY
250	Requested mail action okay, completed
251	User not local; will forward to <forward-path>
252	Cannot VRFY user, but will accept message and attempt delivery
550	Requested action not taken: mailbox unavailable
551	User not local; please try <forward-path>
553	Requested action not taken: mailbox name not allowed
500	Syntax error, command unrecognised
501	Syntax error in parameters or arguments
502	Command not implemented
504	Command parameter not implemented
421	<domain> Service not available, closing transmission channel
EXPN
250	Requested mail action okay, completed
550	Requested action not taken: mailbox unavailable
500	Syntax error, command unrecognised
501	Syntax error in parameters or arguments
502	Command not implemented
504	Command parameter not implemented
421	<domain> Service not available, closing transmission channel
HELP
211	System status, or system help reply
214	Help message
500	Syntax error, command unrecognised
501	Syntax error in parameters or arguments
502	Command not implemented
504	Command parameter not implemented
421	<domain> Service not available, closing transmission channel
NOOP
200	(nonstandard success response, see rfc876)
250	Requested mail action okay, completed
500	Syntax error, command unrecognised
421	<domain> Service not available, closing transmission channel
QUIT
221	<domain> Service closing transmission channel
500	Syntax error, command unrecognised
TURN
250	Requested mail action okay, completed
502	Command not implemented
500	Syntax error, command unrecognised
503	Bad sequence of commands
