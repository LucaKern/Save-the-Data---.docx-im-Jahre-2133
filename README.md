# Docx Date Converter App


 

This simple Application allows users to select a Docx file to be analyzed. The analysis consists of checking if there are any variable fillable fields in the document, replacing them in the XML source code with a static value, and delivering a set of relevant metadata values for the analyzed document. For the first version, the solution will focus only on replacing variable date fields, which would otherwise be automatically filled by Microsoft Word after opening the document. Date values will be replaced by a static date at the time of analysis. This application converts .docx files that have a dynamic date field and saves them with a static date of the data when the .docx was created. It is a solution to the challenge of preserving the integrity of .docx files in archival systems.


 

The solution consists of three parts:

- Front-End (React, Electron)

- API (Python)

- Back-End (Python)


 

![Docx Date Converter](https://github.com/LucaKern/Save-the-Data---.docx-im-Jahre-2133/blob/main/frontend/example_image.png)


 

## The Challenge


 

A large portion of data produced within the Canton Administration is created in the .docx format. Despite .docx being the most frequently used format, it\'s not permitted for archival due to potential inconsistencies across different Word versions and functions (e.g., automatically updated fields) that can lead to mutable content. Therefore, it\'s recommended to convert every Word document to pdf/A-2u for archival purposes, but this conversion leads to information loss.


 

We ask the question: "Could we archive documents in .docx, i.e., in their original format, given that Word has been a prominent document format for 40 years and might continue to be for the next 40 years?"


 

This challenge aims to develop software that performs an analysis of .docx documents, identifies critical elements concerning the mutability of .docx, and creates a new archive-friendly Word document.


 

## Running the Software


 

To run the software, you need to have both Python (for the Flask backend) and Node.js (for the React frontend) installed on your machine.

## Setup

1. Clone this repository:

    ```bash
    git clone git@github.com:LucaKern/Save-the-Data---.docx-im-Jahre-2133.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Save-the-Data---.docx-im-Jahre-2133
    ```

3. Install the Node.js dependencies:

    ```bash
    npm install
    ```

4. Navigate to the backend directory:

    ```bash
    cd ./backend
    ```

5. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

6. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source venv/bin/activate
        ```

7. Install the Python dependencies:

    ```bash
    pip install -r requirements.txt
    ````

8. Navigate to the electron app:

    ```bash
    cd ./frontend
    ```

## Running the App

To start the application, run the following command:

```bash
npm start


 

## Further Case Analysis


 

DOCX files, commonly used for document storage and sharing, may not be optimal for long-term archiving due to several factors:


 

1. Compatibility: DOCX is a file format associated with Microsoft Office applications. While it enjoys widespread support presently, there is no assurance of its future dominance. If you rely on specific software to access DOCX files, there is a risk of obsolescence or incompatibility with newer systems, hindering retrieval of archived documents.


 

2. Backward Compatibility: With each new release, Microsoft Office introduces changes to the DOCX format. Opening older DOCX files with newer Office versions can result in formatting errors, missing content, or altered document layout. Such issues pose challenges when accessing archived files after a significant duration.


 

3. Data Corruption: Over time, files may experience corruption or degradation due to hardware failures, software bugs, or storage media issues. Due to the dependencies and complexity of the DOCX format, it is relatively more susceptible to integrity problems. Repairing corrupted DOCX files can be challenging, potentially leading to data loss or incomplete retrieval of archived documents.


 

4. Long-Term Storage Standards: For long-term archiving, employing open, standardized file formats is recommended. Formats like PDF/A2-u, designed specifically for archiving, ensure document preservation and accessibility over extended periods. These formats are independent of specific software vendors, enhancing compatibility and longevity.


 

While converting important documents to standardized formats like PDF/A2-u is generally advised for long-term archiving, it is worth noting that the widespread use and potential future developments surrounding DOCX could contribute to its acceptance as an archival standard. Factors such as popularity, backward compatibility efforts, support from Microsoft, industry acceptance, and technological advancements might enhance the reliability of DOCX as an archiving format. However, until industry-wide acceptance and preservation efforts validate its suitability, adhering to current best practices by relying on standardized formats like PDF/A2-u for long-term archiving remains a prudent approach.