from typing import Any, Dict, Iterator, List, Mapping, Optional
from langchain_core.callbacks.manager import CallbackManagerForLLMRun
from langchain_core.language_models.llms import LLM
from langchain_core.outputs import GenerationChunk
import requests
import json

class CloudLLM(LLM):
    """A custom LLM that interfaces with a RunPod serverless endpoint.

    This LLM sends requests to a specified RunPod endpoint and processes
    the streaming responses.

    Args:
        endpoint_url: The URL of the RunPod serverless endpoint.
        model: The name of the model to use (e.g., "testforceai/sta_llama3.1").

    Example:
        .. code-block:: python

            llm = CloudLLM(
                endpoint_url="https://{POD-ID}-11434.proxy.runpod.net/api/generate",
                model="testforceai/sta_llama3.1"
            )
            result = llm.invoke("Your prompt here")
    """

    endpoint_url: str
    model: str

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        """Run the LLM on the given prompt.

        Args:
            prompt: The prompt to generate from.
            stop: Stop words to use when generating. Not implemented in this version.
            run_manager: Callback manager for the run.
            **kwargs: Additional keyword arguments passed to the API call.

        Returns:
            The model output as a string.
        """
        if stop is not None:
            raise NotImplementedError("Stop sequences are not implemented for this model.")
        
        response = self._run_generate_request(prompt)
        return response

    def _stream(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> Iterator[GenerationChunk]:
        """Stream the LLM response for the given prompt.

        Args:
            prompt: The prompt to generate from.
            stop: Stop words to use when generating. Not implemented in this version.
            run_manager: Callback manager for the run.
            **kwargs: Additional keyword arguments passed to the API call.

        Yields:
            An iterator of GenerationChunks.
        """
        if stop is not None:
            raise NotImplementedError("Stop sequences are not implemented for this model.")

        headers = {"Content-Type": "application/json"}
        payload = json.dumps({
            "model": self.model,
            "prompt": prompt
        })

        with requests.post(self.endpoint_url, data=payload, headers=headers, stream=True) as response:
            for line in response.iter_lines():
                if line:
                    json_response = json.loads(line)
                    chunk = GenerationChunk(text=json_response.get('response', ''))
                    if run_manager:
                        run_manager.on_llm_new_token(chunk.text, chunk=chunk)
                    yield chunk

    def _run_generate_request(self, prompt: str) -> str:
        """Send a request to the RunPod endpoint and process the response.

        Args:
            prompt: The prompt to send to the model.

        Returns:
            The full response from the model as a string.
        """
        headers = {"Content-Type": "application/json"}
        payload = json.dumps({
            "model": self.model,
            "prompt": prompt
        })
        
        response = requests.post(self.endpoint_url, data=payload, headers=headers)

        if response.status_code == 200:
            json_responses = [json.loads(line) for line in response.text.strip().split('\n')]
            full_response = ''.join(obj['response'] for obj in json_responses if 'response' in obj)
            return full_response
        else:
            raise Exception(f"Error: {response.status_code}\n{response.text}")

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {
            "model_name": f"CloudLLM-{self.model}",
            "endpoint_url": self.endpoint_url
        }

    @property
    def _llm_type(self) -> str:
        """Get the type of LLM."""
        return "cloud_llm"