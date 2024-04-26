# Problem statement 
Automating RFP processing and dispatching proposals to customers through generative ai

## Service architecture

```mermaid  
graph LR
    Customer -->|RFP| API
    API -->|RFP| RFP_processor
    RFP_processor -->|RFP| RFP_parser
    RFP_processor -->|parsed-file-struct| Catalogue_extractor
    RFP_processor -->|approved-product-information| Approval_service
    RFP_parser --> |parsed-file-struct|RFP_processor
    Catalogue_extractor --> RFP_processor
    Catalogue_extractor -->|request for relevant| Catalogue_database
    Catalogue_database -->|request for data| Catalogue_extractor
    Approval_service -->|proposal| RFP_processor
    RFP_processor --> |proposal| API
```
