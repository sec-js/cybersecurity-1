# OWASP Top Ten 2021

The OWASP Top Ten defines the ten most severe web application risks. Secure software development lifecycles should ensure that the OWASP Top Ten vulnerabilities are tested for during the development of a web application. 

### A01 Broken Access Control

Broken access controls refers to a violation of access control policies that describe who has access to a given resource or event. Threat actors who have managed to subvert an applications access controls have gain unauthorized access to resources or have the ability to execute events on the application, i.e., change another users password.

Broken access controls vulnerabilities can be found in many application components such as URL parameters, HTTP requests headers to the web applications API, unsecure pages discoved by forced browsing that require weak or no authentication, etc and can lead to the escalation of privileges, both vertically, i.e., unapproved access to an account with admin priliveges or horizontally, i.e., unapproved access to an account with the same privileges.

#### How to Prevent

- Restrict access to resources or events with proper access control validation checks
- Ensure the principal making a request should be allowed to make the request
- Query parameters that identify resources should be unguessable or easily retrievable, i.e., use UUIDs
- All API calls should be authenticated and authorized before execution

### A02 Cryptographic Failures

Cryptographic failures expose an application to vulnerabilities that allow a threat actor to collect sensitive data, such as **personally identifiably information (PII)**, at rest or in motion. Some cryptographic vulnerabilities can include:

- clear text data transmission
- weak cryptographic algorithms or protocols
- default cryptographic keys, non-rotating encryption keys/initialization vectors
- nonenforcement of encryption via HTTP headers such as HSTS, cookies with the *Secure* attribute
- inproper validation of certificates
- the absence of key derivation functions for generating secret keys from a secret value
- Not using cryptographically secure pseudorandom number generators (CSPRNG)
- deprecated hash functions such as MD5 or SHA1
- exploitable cryptographic error messages or side channel information
- don't write your own cryptographic libraries, rely on the cryptographic libraries that have been scrutinized by renowned cryptologist

#### How to Prevent

- classify data that is processed, stored, and transmitted by an application so that developers understand where secure cryptographic functions are required to ensure sensitive data defined by privacy laws such as GDPR or regulations such as PCI DSS are being followed
- encrypt all data at rest and in transit
- disable caching for responses that contain sensitive information, i.e., `Cache-Control: no-cache, no-store`
- Use secure secure encryption protocols such as TLSv1.2, TLSv1.3
- Use key derivation functions (KDF) for generating cryptographically secure secret keys to use for encryption
- Avoid deprecated security protocols, algorithms

### A03 Injection

Injection vulnerabilities arise when a remote threat actor is able to inject malicious instructions using various languages such as OS commands, SQL, NoSQL, LDAP, JavaScript, etc and execute arbitrary commands on the underlying server. Previously ranked as the #1 threat category of the OWASP Top Ten 2017 list, injection vulnerabilities has fallen two positions down the list due to many modern framekworks that provide strong defences against common injection attacks by providing APIs that perform string sanitization, filtering, and validation of untrusted user input.

#### How to Prevent

The most effective way of preventing injections attacks is via source code review. Automated fuzzing of all hostile application entry points should be performed during the development of an application and after, when more effective fuzzing techniques have been uncovered. Establishing continuous processes intent on application security testing is strongly encouraged and can make a huge difference to the overall security of an application.

### A04 Insecure Design

Insecure design refers to the ineffective design of an applications security defences most likely caused by insufficient threat modeling activities performed during the earlier phases of the software development lifecycle (SDLC). In the OWASP category description for insecure design, they emphasize the distinction between insecure design and insecure implementation by explaining that an application with an insecure design will always remain vulnerable, no matter how secure the implementation is, because its design doesn't account for specific attacks that were never considered during an applications design. OWASPs attributes insecure design to a lack of "business risk profiling" that results in the failure to identify the level of acceptable risks and ultimately the security required by the application.

Secure design is a methodology that should ensure an applications security defences are able to detect and prevent known attack methods which requires continuous threat modeling activities throughout an applications developemnt lifecycle - from the initial design discussions to user acceptance testing (UAT).

#### How to Prevent

- establish a secure software developemnt lifecycle (SSDLC)
- establish and use libraries with secure design patterns
- use threating modeling everywhere and continuously but focus on critical authentication, access controls, business logic, and key flows
- write unit and integration tests

### A05 Security Misconfiguration

Misconfiguring an application or any component of its technology stack is a common way to expose a larger attack surface to threat actors. With so many configurable options, applications are many times configured with settings that may or may not have been set and that undermine the applications defences. Security hardening failures across the application stack, unnecessary enabled options (e.g. redundant ports, services, pages, accounts, etc), default credentials, verbose error handling messages sent in responses to users, security settings of the servers, frameworks, libraries, databases, etc in use are missing, and outdated technologies in use, are some security misconfigurations that leave an application vulnerable to attack.


#### How to Prevent

- an application security configuraton review process must be in place to ensure applications aren't inadvertently introducing security vulnerabilities via configurable options.
- use a platform that requires minimal configuration on behalf of the developer
- do not enable options unless there is a thorough understanding of how that option alters the application
- include configuration reviews into the patch management process
- use automation to check against the effectiveness of an applications current configuration

### A06 Vulnerable and Outdate Components

One easy way to weaken the defences of an application is to unintentionally or intentionally use components with known vulnerabilities - and yes, you read that right, *intentionally*. Why developers might continue to use vulnerable components in their application really comes down to how dependent their application is on that component. For example, maybe the 3rd party validation library an application uses breaks with the current, secure release of the library. A risk assessment would normally need to be performed in such a case to understand the risks involved with keeping the vulnerable component. Decision makers may need to tolerate a high level of risks until a solution is discovered or potentially lose revenue. 

Vulnerable compoments make their way into application because developers might not know the versions of these components, and whether or not they are container known vulnerabilities. Failing to establish processes that scan for known vulnerabilities or test compatibility with updated/uprgraded libraries, also allows vulnerable components to remain in use unknowingly.

#### How to Prevent

- remove unused dependencies, unnecessary features, components, files, documention, etc
- maintain an inventory of all the 3rd component libraries in use
- only use signed components from official sources over secure links
- establish a process to monitor for depencencies that are no longer in use

### A07 Identification and Authentication Failures

Identification and authentication failures allow attackers to carry out identity and authentication related attacks that completely subvert an applications efforts to correctly identify users and limit the access of users to intended resources. Applications that fail to prevent automated attacks such as credentials stuffing or brute force attacks, use default credentials, implement weak credential recovery mechanisms, use insecure communication protocols, fail to provide MFA, improperly invalidate session tokens, etc allow attackers to act on behalf of the identities of privileged or non-privileged users, undermining the application security defences.

#### How to Prevent

- implement proper MFA using 2 of the 3 three factors
  - use time-based one time passwords (TOTPs) or physical security tokens
- ensure default credentials are not in use
- perform checks for weak passwords obtained from data breaches
- enforce a strong password creation policy
- delay authentication attempts incrementally after authentication failures
- use server-side session management libraries that generate random session IDs

### A08 Software and Data Integrity Failures

With the growing use of CI/CD pipelines, infrastructure-as-code (IoC), and automation, identifying integrity failures is crucial to prevent attacks against infrastructure and application development and deployment workflows. Because so many components of an application now rely on dependencies that are no longer internally developed, maintained, and stored, developers are left to rely on the security implemented by 3rd parties. Components such as plugins, libraries, modules can all come from untrusted sources, repositories, and content delivery networks (CDNs) which means secure integrity verification procedures need to be created to catch malicious components attempting to gain access to an application or its technology stack.

#### How to Prevent

- use digital signatures to verify software and data is originating from trusted parties
- use internally hosted code repositories when possible, if not, ensure dependency fetching tools (pip, npm) are consuming trusted repositories
- use software supply chain tools to search dependencies for known vulnerabilities
- code and configuration changes should be vetted by several individuals before being making it to production
- CI/CD pipelines should have secure flow control mechanisms, configurations, and access controls to ensure the integrity of changes being sent through the build and deploy process

### A09 Security Logging and Monitoring Failures

#### How to Prevent

### A10 Server-side Request Forgery

Server-side Request Forgery (SSRF) allows an attacker to control the destination URL of a resource, coercing the application to make requests on behalf of the attacker. SSRF arises in applications that fail to validate user-supplied URLs in services. With the growing implementation of microservice architectures, SSRF is becoming more ubiquitous because of the decoupled nature of microservices and there dependence on remotely deployed components that create opportunities for attackers to hijack the request to these components.

SSRF can also be used to carry out attacks against other organizations resources such as DOS attacks and because requests are originating from the vulnerable application, an attacker can make it appear as if one organization is DOSing another. 

#### How to Prevent

*At the Network Layer*

- segment remote resources into seperate networks
- create "deny by default" firewall policies for traffic that does match intended behavior

*At the Application Layer*

- sanitize and validate all user-supplied input data specifically where the user is allowed to specify a URL
- use URL allows list to validate user-supplied URLs
- disable HTTP redirections
- **DON'T** use blacks or regular expressions to attempt to mitigate SSRF because attackers can find ways to bypass these filters
