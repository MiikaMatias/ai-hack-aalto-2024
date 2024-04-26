

```mermaid  
graph LR
    Customer -->|RFP| API
    API -->|RFP| RFP_processor
    RFP_processor -->|RFP| RFP_parser
    RFP_processor -->|parsed-file-struct| Catalogue_extractor
    RFP_processor -->|approved-product-information| Approval_service
    RFP_parser --> |parsed-file-struct|RFP_processor
    Catalogue_extractor --> RFP_processor
    Approval_service -->|proposal| RFP_processor
    RFP_processor --> |proposal| API
```
