import math
from decimal import Decimal

from ..order import Order
from ..trading_signal import TradingSignal
from .funds_allocator import FundsAllocator
from .kite_broker import KiteBroker
from .singleton_maker import Singleton


class OrderPlacer(metaclass=Singleton):
    funds_allocator: FundsAllocator = None
    kite: KiteBroker = None

    def __init__(self):
        self.funds_allocator = FundsAllocator()
        self.kite = KiteBroker()

    def process_signal(self, trading_signal: TradingSignal) -> None:
        """process

        gets called from TradingSystem -> OrderPlacer.process_signal(trading_signal)
        """

        order_id_at_broker = self.place_options_order_at_broker(trading_signal)
        print(f"------- order_id_at_broker: {order_id_at_broker}")

        order_object = self.record_order_details_from_broker(
            order_id_at_broker, trading_signal
        )
        print(f"------- order_object= {order_object}")

        self.install_order_updates_for(order_object)

        self.update_objects_with_order_details(trading_signal, order_object)

        return order_object.id

    def place_options_order_at_broker(self, trading_signal: TradingSignal) -> int:
        funds_for_trade = self.funds_allocator.get_permissible_funds(trading_signal)

        (margin_required_per_lot, last_known_ltp) = self.get_ltp_and_margin_per_lot(
            trading_signal
        )

        lots_to_take = math.floor(funds_for_trade / margin_required_per_lot)

        return self.kite.place_options_order(
            trading_signal, lots_to_take, last_known_ltp
        )

    def get_ltp_and_margin_per_lot(self, trading_signal: TradingSignal) -> Decimal:
        broker_symbol = trading_signal.symbol_for_broker_query()
        last_known_ltp = self.kite.last_known_ltp(broker_symbol)

        return (last_known_ltp * trading_signal.lot_size, last_known_ltp)

    def record_order_details_from_broker(
        self, order_id_at_broker: int, trading_signal: TradingSignal
    ) -> Order:
        order_history = self.kite.order_history(order_id_at_broker)["data"]

        order = Order.objects.update_details_and_history(order_history, trading_signal)
        return order

    def install_order_updates_for(self, order_object: Order) -> None:
        return "install kite listeners"

    def update_objects_with_order_details(
        self, trading_signal: TradingSignal, order_object: Order
    ) -> None:
        return "update Tsig status, attach order to Tsig"