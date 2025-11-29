# SafeDrive-Platform
The project realizes a service-oriented architecture (SOA) using four heterogeneous protocols (SOAP, REST, GraphQL, gRPC) and applies the complete DevOps methodologies, including containerization, CI/CD, observability and security scans.

SafeDrive-Platform/
├── .github/workflows/     <-- (DEVOPS) Pipeline CI/CD
├── ia-service/            <-- (IA & SOA) Microservice gRPC (Python)
├── cyber-service/         <-- (CYBER & SOA) Microservice REST (Python)
├── driver-api/            <-- (SOA) Microservice GraphQL (Node.js)
├── legacy-weather/        <-- (SOA) Microservice SOAP (Python)
├── api-gateway/           <-- (SOA) Point d'entrée unique (Python/FastAPI)
├── frontend/              <-- (SOA) Dashboard React
├── k8s/                   <-- (DEVOPS) Fichiers Kubernetes
└── docker-compose.yml     <-- (DEVOPS) Pour lancer tout en un clic
