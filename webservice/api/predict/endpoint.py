from fastapi import APIRouter, Request

from nuvox_algorithm.core import TracePoint, nuvox_keyboard
from .models import PredictRequest, PredictResponse

router = APIRouter()


@router.post('/predict/', response_model=PredictResponse)
def predict(request: Request, body: PredictRequest) -> PredictResponse:
    trace = [
        TracePoint(**point.dict(), key_id=nuvox_keyboard.key_at_point(point.x, point.y).id)
        for point in body.trace
    ]

    if (trace[0].key_id != '5') and (trace[-1].key_id == '5'):
        # If user starts a valid word but ends in key 5 then this means
        # they made a mistake so predict no words.
        action = None
        predicted_words = []
    elif (trace[0].key_id == '5' and trace[-1].key_id == '5') and (trace[-1].x < trace[0].x):
        # If user swipes leftward inside key 5 this means delete.
        action = 'delete'
        predicted_words = []
    else:
        # Perform actual prediction.
        action = 'type'
        predicted_words = request.app.state.nuvox_algorithm.predict(prompt=body.prompt, trace=trace)

    return PredictResponse(
        action=action,
        words=predicted_words,
    )
