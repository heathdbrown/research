# Python Logging for an Application

## Tip #1 from MCoding: Use DictConfig instead of Basicconfig
- https://youtu.be/9L77QExPmI0?t=128

```python
import logging.config

logger.getLogger("my_app")

logging_config = {
   "version": 1,
   "disable_existing_loggers" : False,
   "filters" : {},
   "formatteres" : {},
   "handlers" : {},
   "loggers" : {}
}

def main():
   logging.config.dictConfig(config=logging_config)
   ...
```

## Tip #2 from Mcoding: PUt all handlers/filters on the root
- https://youtu.be/9L77QExPmI0?t=380

## Tip #3 from Mcoding: Don't use the root logger
- https://youtu.be/9L77QExPmI0?t=411

```python
#mocding example see youtube link above
logging.info("uses root logger") #BAD
logger = logging.getLogger("myapp") # User your own logger, Good
```

## Tip #4 from Mcoding: One Logger per Major Subcomponent
- don't getLogger(__name__) in every file
- https://youtu.be/9L77QExPmI0?t=461

## Tip #5 from MCoding: Instead of inside the Python application as a dict you can read in configuration from file

- Store as JSON or YAML
- Parse configuration

Example: config.json
```json
{
   "version": 1,
   "disable_existing_loggers" : False,
   "formatteres" : {
       "simple" : {
           "format" : "%(levelname)s: %(message)s",
       }
   },
   "handlers" : {
       "stdout": {
           "class": "logging.StreamHandler",
           "formatter": "simple",
           "stream": "ext://sys.stdout",
       }
   },
   "loggers" : {
       "root": {"level": "DEBUG", "handlers": ["stdout"]}
   }
}

```

## Tip #6 from Mcoding:

## Tip #7 from Mcoding: Store Persistent logs in JSON
- https://youtu.be/9L77QExPmI0?t=772
- Write a custom Handler that generates JSON strings

## Tip #8 from Mcoding: 

## Tip #9 from Mcoding: Log off the main thread

### Multiple Handlers for STDOUT, STDERR, File, and JSON

#### STDOUT

```python
logging_config = {
   "version": 1,
   "disable_existing_loggers" : False,
   "formatteres" : {
       "simple" : {
           "format" : "%(levelname)s: %(message)s",
       }
   },
   "handlers" : {
       "stdout": {
           "class": "logging.StreamHandler",
           "formatter": "simple",
           "stream": "ext://sys.stdout",
       }
   },
   "loggers" : {
       "root": {"level": "DEBUG", "handlers": ["stdout"]}
   }
}
```

#### STDERR

#### File

#### JSON

# Tip #10 from Mcoding: For Libraries Don't configure logging
should not have configuration
You can have logging and handlers but no 'configuration'

# Remember log4j!
- Don't log user input (avoid makeLogRecord)
- If you do NEED to sanitize the input before logging
- DO NOT send python objects to logging as pickle 

# References
- https://www.youtube.com/watch?v=9L77QExPmI0&t
- https://github.com/mCodingLLC/VideosSampleCode