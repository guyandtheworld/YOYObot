from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities  import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities      import OutgoingAckProtocolEntity
import re


class EchoLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        #send receipt otherwise we keep receiving the same message over and over
        if True:
            receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(), 'read', messageProtocolEntity.getParticipant())
            if hasattr(messageProtocolEntity, 'mimeType'):
                pass
            else:
                outgoingMessageProtocolEntity = TextMessageProtocolEntity(
                    messageProtocolEntity.getBody(),
                    to = messageProtocolEntity.getFrom())

                if re.match(r'[\w.-]+@g.us', outgoingMessageProtocolEntity.to):
                    pass
                else:
                    print(vars(outgoingMessageProtocolEntity))
                    outgoingMessageProtocolEntity.to = "918089137055-1496481373@g.us"
                    outgoingMessageProtocolEntity.body = "*Anonymous User* : " + outgoingMessageProtocolEntity.body
                    self.toLower(receipt)
                    self.toLower(outgoingMessageProtocolEntity)

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        ack = OutgoingAckProtocolEntity(entity.getId(), "receipt", entity.getType(), entity.getFrom())
        self.toLower(ack)

    # @ProtocolEntityCallback("success")
    # def onSuccess(self, successProtocolEntity):

    #     entity = PresenceProtocolEntity(name = "YOYObot.")
    #     self.toLower(entity)