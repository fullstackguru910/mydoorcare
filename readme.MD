
1. User Management APIs:
• Account Creation:

• Endpoint: POST /api/users/register
• Description: Allows new users to create an account by providing necessary details.
• Parameters:
• username (string)
• email (string)
• password (string)
• role (string) – e.g., ‘user’ or ‘service_provider’

• Response:
• userId (string)
• message (string) – Success or error message

• Login:

• Endpoint: POST /api/users/login
• Description: Authenticates users and returns a token for authorized access.
• Parameters:
• email (string)
• password (string)
• Response:
• token (string)
• userId (string)
• message (string) – Success or error message

• Complete Profile with Image Upload:

• Endpoint: PUT /api/users/{userId}/profile
• Description: Allows users to complete or update their profile, including uploading a profile image.
• Parameters:
• fullName (string)
• phoneNumber (string)
• address (string)
• profileImage (file)
• Response:
• message (string) – Success or error message


2. Worker Management APIs:

• Get All Workers:

• Endpoint: GET /api/workers
• Description: Retrieves a list of all available workers to display on the home screen.
• Parameters:
• Optional filters: serviceType, location, etc.
• Response:
• workers (array) – List of worker objects

• Book Worker:

• Endpoint: POST /api/workers/{workerId}/book
• Description: Allows users to book a specific worker for a service.
• Parameters:
• userId (string)
• serviceDetails (string)
• scheduledTime (datetime)
• Response:
• bookingId (string)
• message (string) – Success or error message

• Accept Invitation:

• Endpoint: POST /api/workers/{workerId}/invitations/{invitationId}/accept
• Description: Allows workers to accept service invitations.
• Parameters:
• workerId (string)
• invitationId (string)
• Response:
• message (string) – Success or error message

• Edit Profile:

• Endpoint: PUT /api/workers/{workerId}/profile
• Description: Enables workers to update their profile information.
• Parameters:
• fullName (string)
• phoneNumber (string)
• servicesOffered (array)
• profileImage (file)
• Response:
• message (string) – Success or error message


3. Chat and Communication APIs:

• Initialize Chat Session:

• Endpoint: POST /api/chat/initiate
• Description: Starts a chat session between a user and a service provider.
• Parameters:
• userId (string)
• serviceProviderId (string)
• Response:
• chatSessionId (string)
• message (string) – Success or error message

• Send Message:

• Endpoint: POST /api/chat/{chatSessionId}/message
• Description: Sends a message within an active chat session.
• Parameters:
• senderId (string)
• messageContent (string)
• Response:
• messageId (string)
• timestamp (datetime)

• Real-time Communication:

• Description: Implement WebSocket connections for real-time chat functionality.
• Protocol: WebSocket
• Endpoints:
• /ws/chat/{chatSessionId}



4. Ride Booking and Management APIs:

• Fetch Address:

• Endpoint: GET /api/locations/address
• Description: Retrieves address details based on coordinates or place ID.
• Parameters:
• latitude (float)
• longitude (float)
• Response:
• address (string)

• Route Finding and Polyline Generation:

• Endpoint: GET /api/routes
• Description: Calculates the optimal route and generates a polyline image.
• Parameters:
• startLocation (string)
• endLocation (string)
• Response:
• routeDetails (object)
• polylineImage (string) – URL or base64 encoded image
• Calculate Distance and Price: