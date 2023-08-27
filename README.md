![Neploy Banner](neploy_banner.png)
# Neploy

### Simplifying Neo3 Smart Contract Deployment and Testing
Welcome to the official repository of **Neploy**, a  path breaking innovative project submitted under the Infrastructure and Tooling category for the 2023 NEO APAC Hackathon. Neploy aims to revolutionize the process of compiling, reviewing, testing, and deploying NEO smart contracts written in Python (Using [neo3-boa](https://github.com/CityOfZion/neo3-boa) package), all while eliminating the complexities of setting up the development environment with NEO blockchain toolkits.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [AI-Powered Code Review](#ai-powered-code-review)
- [License](#license)

## Project Overview

Neploy addresses the common challenges faced by developers when it comes to working with NEO smart contracts. Compiling, deploying, and testing these contracts manually can be time-consuming and error-prone as it requires cubersome steps for setting up the local environment. Neploy simplifies this process by providing an intuitive web portal that interacts with a Kubernetes-based backend to streamline the entire workflow.

## Features

- **User-Friendly Portal:** Neploy offers a user-friendly web portal that allows developers to effortlessly deploy their NEO smart contracts without the need for intricate setup steps.

- **Automated Compilation:** The smart contract deployment process includes automated compilation, ensuring that the code is error-free before being sent to the blockchain.

- **Effortless Testing:** Developers can easily test their smart contracts within the Neploy environment, enabling rapid iteration and bug detection.

- **AI-Powered Code Review:** Neploy leverages AI/ML to provide code optimization suggestions, enhancing the quality and efficiency of the smart contracts.

## Technology Stack

- **Backend:** Kubernetes is utilized to containerize the backend applications written in Python, ensuring scalability and efficient resource management. Currently, the backend applications include feature for compiling code, and review code using AI/ML model.

- **Frontend:** The frontend is developed using JavaScript, providing a seamless interface for users to interact with the backend's exposed endpoints.

## Getting Started

Follow these steps to get started with Neploy:

1. Clone the repository: `git clone https://github.com/lokeshwaran100/neploy.git`
2. Navigate to the project directory: `cd neploy`
3. Follow the [procedure](https://github.com/lokeshwaran100/neploy/blob/main/src/backend/README.md) to set up the Kubernetes environment for the backend. 
4. Follow the [procedure](https://github.com/lokeshwaran100/neploy/blob/main/src/frontend/README.md) to launch the frontend application in your preferred web browser.

## Usage

1. Access the Neploy web portal.
2. Write your Python-based ([neo3-boa](https://github.com/CityOfZion/neo3-boa)) NEO smart contract.
3. Compile the written smart contracts.
4. Review the written smart contracts with AI/ML.

## AI-Powered Code Review

Neploy incorporates advanced AI/ML algorithms to perform code reviews for submitted smart contracts. This feature provides optimization suggestions, enabling developers to enhance their contracts for improved performance and efficiency.

## License

Neploy is released under the [MIT License](LICENSE).

---

*Disclaimer: This project was created for the 2023 NEO APAC Hackathon.*
